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
		self.tool = None
		self.required_tool = None

	def __str__(self):
		if self.has_tool():
			return "Worker (Tool: " + str(self.tool) + " / Workspeed = " + str(self.work_speed) + ") : " + People.__str__(self)
		else:
			return "Worker (Requires: " + str(self.require_tool()) + " / Workspeed = " + str(self.work_speed) + ") : " + People.__str__(self)
	
	def has_tool(self):
		if self.required_tool:		
			if isinstance(self.tool, self.required_tool):
				return True

		return False
	
	def require_tool(self):
		if self.has_tool():
			return None
		else:
			return tools.Spade

	def work(self, ticks, building):
		pass




class Flattener(Worker): # Planierer
	""" Flattens ground for building """
	def __init__(self):
		Worker.__init__(self)
		self.work_speed = 5
		self.required_tool = tools.Spade

	def work(self, ticks, building):
		if self.has_tool() != True: return

		diff = ticks - self.ticks
		if diff > self.work_speed:
			self.ticks = ticks
			if building.built < 20:
				building.built += (diff/self.work_speed)
			
			if building.built > 100:
				building.built = 100

	def __str__(self):
		return "Flattener : " + Worker.__str__(self)



class Builder(Worker): # Bauarbeiter
	def __init__(self):
		Worker.__init__(self)
		self.work_speed = 3
		self.required_tool = tools.Hammer

	def work(self, ticks, building):
		if self.has_tool() != True: return

		diff = ticks - self.ticks
		if diff > self.work_speed:
			self.ticks = ticks
			if building.built in range(20, 99):
				building.built += (diff/self.work_speed)
			
			if building.built > 100:
				building.built = 100

	def __str__(self):
		return "Builder : " + Worker.__str__(self)



class Lumberjack(Worker):
	def __init__(self):
		Worker.__init__(self)
		self.work_speed = 35
		self.required_tool = tools.Axe

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
	f = Flattener()
	print "\t" + str(f)
	b = buildings.LumberjackHouse()
	print "\t" + str(b)
	
	print ""
	print "\tBeginning to work..."
	print ""
	print "\t" + str(b)
	for i in range(1,22): f.work(10*i, b)
	print "\t" + str(b)

	f.tool = tools.Spade()
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
	b = Builder()
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

	b.tool = tools.Hammer()
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
