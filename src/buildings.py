__author__="Yves Adler"
__date__ ="$Nov 5, 2009 3:09:20 PM$"

import people


class Building:
	""" Base class for all buildings """
	def __init__(self):
		self.built = 0

	def __str__(self):
		return "Building ("  + str(self.built) + "% built / Needs: " + str(self.requires_people()) + ")"

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
	
	def requires_people(self):
		""" returns what kind of people is desired by this building"""
		if self.is_built():
			return None
		elif self.is_flattened():
			return people.Builder
		else:
			return people.Flattener



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

	def __str__(self):
		return  "LumberjackHouse : " + SmallBuilding.__str__(self)

	def requires_people(self):
		if SmallBuilding.requires_people(self):
			return SmallBuilding.requires_people(self)
		else:
			return people.Lumberjack






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

	# fuer pool
	print l.requires_people()
	new_worker = l.requires_people()()
	print new_worker
	print isinstance(new_worker, l.requires_people())

if __name__ == "__main__":
	test_building()
	test_lumberjack_house()