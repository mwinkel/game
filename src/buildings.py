__author__="Yves Adler"
__date__ ="$Nov 5, 2009 3:09:20 PM$"

import people


class Building:
	""" Base class for all buildings """
	def __init__(self):
		self.built = 0
		self.inhabitant = None
		self.required_people = None

	def __str__(self):
		if self.has_people():
			return "Building ["  + str(self.built) + "% built] Inhabitant: " + str(self.inhabitant)
		else:
			return "Building ["  + str(self.built) + "% built] Needs: " + str(self.requires_people())

	def is_flattened(self):
		if self.built < 20:
			return False
		else:
			return True

	def is_built(self):
		if self.built < 100:
			return False
		else:
			return True

	def has_people(self):
		if self.required_people != None:
			if isinstance(self.inhabitant, self.required_people):
				return True
		
		return False

	def requires_people(self):
		""" returns what kind of people is desired by this building"""
		if self.has_people():
			return None
		
		if self.is_built():
			return self.required_people
		elif self.is_flattened():
			return people.Builder
		else:
			return people.Flattener

	def work(self, ticks):
		if self.has_people():
			self.inhabitant.work(ticks, self)



class SmallBuilding(Building):
	""" Base class for small buildings """
	def __init__(self):
		Building.__init__(self)

	def __str__(self):
		return  "SmallBuilding : " +  Building.__str__(self)



class LumberjackHouse(SmallBuilding):
	""" Lumberjack building to get some wood """

	def __init__(self):
		SmallBuilding.__init__(self)
		self.required_people = people.Lumberjack

	def __str__(self):
		return  "LumberjackHouse : " + SmallBuilding.__str__(self)





def test_building():
	print "Testing Building:"
	b = Building()
	print "\t" + str(b)
	print "\tBuilding built to " + str(b.built) + "%"
	print "\tBuilding finished : " + str(b.is_built())
	print "\tBuilding needs following people : " + str(b.requires_people())

def test_lumberjack_house():
	print ""
	print "Testing Lumberjack House:"
	l = LumberjackHouse()
	print "\t" + str(l)
	l.built = 20
	print "\t" + str(l)
	l.built = 100
	print "\t" + str(l)
	l.inhabitant = people.Lumberjack()
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

if __name__ == "__main__":
	test_building()
	test_lumberjack_house()