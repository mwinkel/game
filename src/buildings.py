from gameobject import *
import copy
import goods
import tools
import people
import balance

__author__="Yves Adler"
__date__ ="$Nov 5, 2009 3:09:20 PM$"


class Building(Gameobject):
	""" Base class for all buildings """
	def __init__(self):
		self._built = 0.0
		self._building_time = 0.0
		self._inhabitant = None
		self._required_people = None
		self._required_goods = []
		self._building_costs = []
		self._consumed_materials = []
		self._goods = []

	def __str__(self):
		return_string =  "Building ["  + str(self._built) + "% built]"
		
		if self.has_working_people() or self.has_building_people():
			return_string += " --- Inhabitant: " + str(self._inhabitant)
		else:
			return_string += " --- Needs people: " + str(self.requires_people())

		if self.requires_goods():
			return_string += " --- Needs goods: " +  str(self.requires_goods())
		
		return return_string

	def accepts_goods(self):
		if len(self._goods) < balance.MAX_GOODS_AT_BUILDING:
			return True
		else:
			return False

	def add_good(self, good):
		self._goods.append(good)

	def is_flattened(self):
		if self._built < balance.PERCENT_UNTIL_FLATTENED:
			return False
		else:
			return True

	def is_built(self):
		if self._built < 100:
			return False
		else:
			return True

	def has_working_people(self):
		if self._required_people != None:
			if isinstance(self._inhabitant, self._required_people):
				return True
		
		return False

	def has_build_material(self):
		for cost in self._building_costs:
			for good in self._goods:
				if isinstance(good, cost):
					return True

		return False

	def has_building_people(self):
		if self.requires_people():
			return isinstance(self._inhabitant, self.requires_people())
		else:
			return False

	def get_building_time(self):
		return self._building_time

	def get_built_percent(self):
		return self._built

	def inc_built_percent(self, amount):
		self._built += amount
		if self._built > 100:
			self._built = 100

		build_step = (100 - balance.PERCENT_UNTIL_FLATTENED) / (len(self._building_costs) + len(self._consumed_materials))
		next_step = 100 - len(self._building_costs) * build_step

		if self._built >= next_step:
			if self._goods:
				good = self._goods.pop()
				not_removed = True

				for cost in self._building_costs:
					if isinstance(good, cost):
						self._consumed_materials.append(cost)
						self._building_costs.remove(cost)
						not_removed = False

				if not_removed:
					self._goods.append(good)
					self._built = next_step
			else:
				self._built = next_step


	def set_inhabitant(self, inhabitant):
		self._inhabitant = inhabitant
		print self.__str__()
	
	def requires_people(self):
		""" returns what kind of people is desired by this building"""
		if self.has_working_people():
			return None
		
		if self.is_built():
			return self._required_people
		elif self.is_flattened():
			return people.Builder
		else:
			return people.Flattener

	def __requires_build_goods(self):
		still_required = copy.deepcopy(self._building_costs)
		
		for cost in still_required:
			for good in self._goods:
				if isinstance(good, cost):
					still_required.remove(cost)
					break
					
		return still_required

	def requires_goods(self):
		if self.is_built():
			return self._required_goods
		else:
			return self.__requires_build_goods()

	def work(self, ticks):
		if self.has_working_people() or self.has_building_people():
			self._inhabitant.work(ticks, self)




class SmallBuilding(Building):
	""" Base class for small sized buildings """
	def __init__(self):
		Building.__init__(self)

	def __str__(self):
		return  "SmallBuilding : " +  Building.__str__(self)



class MediumBuilding(Building):
	""" Base class for medium sized buildings """
	def __init__(self):
		Building.__init__(self)

	def __str__(self):
		return  "MediumBuilding : " +  Building.__str__(self)



class LargeBuilding(Building):
	""" Base class for large buildings """
	def __init__(self):
		Building.__init__(self)

	def __str__(self):
		return  "LargeBuilding : " +  Building.__str__(self)



class LumberjackHouse(SmallBuilding):
	""" Lumberjack building to get some wood """

	def __init__(self):
		SmallBuilding.__init__(self)
		self._required_people = people.Lumberjack
		self._building_time = balance.BUILDTIME_LUMBERJACK_HOUSE
		self._building_costs = balance.COSTS_LUMBERJACK_HOUSE

	def __str__(self):
		return  "LumberjackHouse : " + SmallBuilding.__str__(self)


class Warehouse(MediumBuilding):
	""" Lumberjack building to get some wood """

	def __init__(self):
		MediumBuilding.__init__(self)
		self._required_people = None
		self._building_time = balance.BUILDTIME_WAREHOUSE
		self._building_costs = balance.COSTS_WAREHOUSE

	def __str__(self):
		return  "Warehouse : " + MediumBuilding.__str__(self)



def test_build_house(house):
	print ""
	flattener = people.Flattener(people.Worker())
	flattener.set_tool(tools.Spade())
	house.set_inhabitant(flattener)
	print "\t" + str(house)
	house.work(200)
	
	print ""
	builder = people.Builder(flattener)
	builder.set_tool(tools.Hammer())
	house.set_inhabitant(builder)
	print "\t" + str(house)	
	house.work(700)
	print "\t" + str(house)

def test_warehouse():
	print "Testing Warehouse:"
	house = Warehouse()
	print "\t" + str(house)
	test_build_house(house)
	
def test_building():
	print "Testing Building:"
	b = Building()
	print "\t" + str(b)
	print "\tBuilding built to " + str(b.built) + "%"
	print "\tBuilding finished : " + str(b.is_built())
	print "\tBuilding needs following people : " + str(b.requires_people())

def test_lumberjack_house2():
	print ""
	print "Testing Lumberjack House (2):"
	house = LumberjackHouse()
	print "\t" + str(house)

	test_build_house(house)

	print ""

	lumberjack = people.Lumberjack(people.Worker())
	lumberjack.set_tool(tools.Axe())
	house.set_inhabitant(lumberjack)
	print "\t" + str(house)
	house.work(20)
	print "\t" + str(house)

def test_lumberjack_house():
	print ""
	print "Testing Lumberjack House:"
	l = LumberjackHouse()
	print "\t" + str(l)
	l.built = 20
	print "\t" + str(l)
	l.built = 100
	print "\t" + str(l)
	l.set_inhabitant(people.Lumberjack(people.Worker()))
	print "\t" + str(l)
	l.work(10)
	l.work(10)

	# fuer pool
#	print "--pool--"
#	l.inhabitant = None
#	print l.requires_people()
#	print l.has_people()
#	print l
#	new_worker = l.requires_people()()
#	print new_worker
#	print isinstance(new_worker, l.requires_people())

def test_build_costs():
	house = LumberjackHouse()
	print house
	house.add_good(goods.Plank())
	print house
	house.add_good(goods.Stone())
	print house
	house.add_good(goods.Stone())
	print house
	house.add_good(goods.Plank())
	print house

if __name__ == "__main__":
#	test_building()
#	test_warehouse()
#	test_lumberjack_house()
#	test_lumberjack_house2()
	test_build_costs()