__author__="Yves Adler"
__date__ ="$Nov 5, 2009 3:10:01 PM$"

import tools
import buildings
import balance


class People(object):
	""" Base class for all people """
	def __init__(self):
		self._ticks = 0
		self.walk_speed = 1

	def __str__(self):
		return "People ( Walkspeed = " + str(self.walk_speed) + ")"



class Soldier(People):
	""" Base class for all fighting people """
	pass



class Worker(People):
	""" Base class for all working people """
	
	def __init__(self, worker=None):
		People.__init__(self);
		self._work_speed = 0
		self._tool = None
		self._required_tool = None
		if worker:
			self._tool = worker.tool

	def __str__(self):
		if self.has_tool():
			return "Worker (Tool: " + str(self._tool) + " / Workspeed = " + str(self._work_speed) + ") : " + People.__str__(self)
		else:
			return "Worker (Requires: " + str(self.require_tool()) + " / Workspeed = " + str(self._work_speed) + ") : " + People.__str__(self)
	
	def has_tool(self):
		if self._required_tool:
			if isinstance(self._tool, self._required_tool):
				return True

		return False

	def set_tool(self, tool):
		self._tool = tool

	def get_tool(self, tool):
		return self._tool

	def require_tool(self):
		if self.has_tool():
			return None
		else:
			return tools.Spade

	def work(self, ticks, building):
		pass




class Flattener(Worker): # Planierer
	""" Flattens ground for building """
	def __init__(self, worker=None):
		Worker.__init__(self)
                if worker:
                    self.__dict__.update(worker.__dict__) # copy instance variables
                
		self._work_speed = 5
		self._required_tool = tools.Spade

	def work(self, ticks, building):
		if self.has_tool() != True: return

		diff = float(ticks - self._ticks)
		work_speed = float(self._work_speed)

		if diff > work_speed:
			self._ticks = ticks
			if building.built < balance.PERCENT_UNTIL_FLATTENED:
				building.built += (diff/work_speed) * (100.0/float(building.get_building_time()))

			if building.built > balance.PERCENT_UNTIL_FLATTENED:
				building.built = balance.PERCENT_UNTIL_FLATTENED


	def __str__(self):
		return "Flattener : " + Worker.__str__(self)



class Builder(Worker): # Bauarbeiter
	def __init__(self, worker=None):
		Worker.__init__(self)
                if worker:
                    self.__dict__.update(worker.__dict__) # copy instance variables
                
		self._work_speed = 3
		self._required_tool = tools.Hammer

	def work(self, ticks, building):
		if self.has_tool() != True: return

		diff = float(ticks - self._ticks)
		work_speed = float(self._work_speed)

		if diff > work_speed:
			self._ticks = ticks
			if building.built in range(balance.PERCENT_UNTIL_FLATTENED, 99):
				building.built += (diff/work_speed) * (100.0/float(building.get_building_time()))
			
			if building.built > 100:
				building.built = 100

	def __str__(self):
		return "Builder : " + Worker.__str__(self)



class Lumberjack(Worker):
	def __init__(self, worker=None):
		Worker.__init__(self)
                if worker:
                    self.__dict__.update(worker.__dict__) # copy instance variables

		self._work_speed = 35
		self._required_tool = tools.Axe

	def __str__(self):
		return "Lumberjack : " + Worker.__str__(self)

	def work(self, ticks, building):
		print "HACK HACK HACK"



def test_worker():
	print "Testing Worker:"
	w = Worker()
	print "\t" + str(w)


def test_flattener():
	print "Testing Flattener:"
	f = Flattener(Worker())
	print "\t" + str(f)
	b = buildings.Warehouse()
	print "\t" + str(b)
	
	print ""
	print "\tBeginning to work..."
	print ""
	print "\t" + str(b)
	for i in range(1,22): f.work(10*i, b)
	print "\t" + str(b)

	f.set_tool(tools.Spade())
	print ""
	print "\tBeginning to work... (this time with tool)"
	print "\t" + str(f)
	print ""
	print "\t" + str(b)
	for i in range(1,22):
		f.work(10*i, b)
		print "\t" + str(b)

def test_builder():
	print "Testing Builder:"
	b = Builder(Worker())
	print "\t" + str(b)
	h = buildings.LumberjackHouse()
	h.built = 20
	print "\t" + str(h)

	print ""
	print "\tBeginning to work..."
	print ""
	print "\t" + str(h)
	for i in range(1,22): b.work(10*i, h)
	print "\t" + str(h)

	b.set_tool(tools.Hammer())
	print ""
	print "\tBeginning to work... (this time with tool)"
	print ""
	print "\t" + str(h)
	for i in range(1,102): b.work(10*i, h)
	print "\t" + str(h)


if __name__ == "__main__":
	test_worker()
	print ""
	test_flattener()
	print ""
	test_builder()
