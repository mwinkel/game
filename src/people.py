__author__="Yves Adler"
__date__ ="$Nov 5, 2009 3:10:01 PM$"

import tools
import buildings


class People:
	""" Base class for all people """
	def __init__(self):
		self.ticks = 0
		self.walk_speed = 1

	def __str__(self):
		return "People ( Walkspeed = " + str(self.walk_speed) + ")"



class Soldier(People):
	""" Base class for all fighting people """
	pass



class Worker(People):
	""" Base class for all working people """
	def __init__(self):
		People.__init__(self);
		self.work_speed = 0

	def require_tool(self):
		return None
	
	def work(self, building):
		pass

	def __str__(self):
		return "Worker (Requires: " + str(self.require_tool()) + " / Workspeed = " + str(self.work_speed) + ") : " + People.__str__(self)



class Flattener(Worker): # Planierer
	""" Flattens ground for building """
	def __init__(self):
		Worker.__init__(self)
		self.work_speed = 5
		self.tool = None

	def require_tool(self):
		if self.tool == None:
			return tools.Spade
		else:
			return None

	def work(self, ticks, building):
		if ticks - self.ticks > self.work_speed:
			self.ticks = ticks
			if building.built < 20:
				building.built += 1
				

	def __str__(self):
		return "Flattener : " + Worker.__str__(self)



class Builder(Worker): # Bauarbeiter
	pass

class Lumberjack(Worker):
	def __init__(self):
		Worker.__init__(self)

	def __str__(self):
		return "Lumberjack : " + Worker.__str__(self)




def test_worker():
	print "Testing Worker:"
	w = Worker()
	print "\t" + str(w)


def test_flattener():
	print "Testing Flattener:"
	f = Flattener()
	print "\t" + str(f)
	b = buildings.LumberjackHouse()
	print "\t" + str(b)
	
	print ""
	print "\tBeginning to work..."
	print ""
	for i in range(1,22):
		f.work(10*i, b)
		print "\t" + str(b)



if __name__ == "__main__":
	test_worker()
	print ""
	test_flattener()
