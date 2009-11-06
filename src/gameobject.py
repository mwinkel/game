
__author__="Yves Adler"
__date__ ="$Nov 5, 2009 3:10:01 PM$"

class Gameobject(object):
	def __init__(self):
		self._position = Position()
		self._target = None

	def get_target(self):
		return _target

	def set_target(self, target):
		self._target = target

	def __str__(self):
		return "Gameobject (Position: " + str(self._position) + ")"


class Position(object):
	def __init__(self):
		self.x = 0.0
		self.y = 0.0
		self.z = 0.0

	def __str__(self):
		return "Position [x=" + str(self.x) + ",y=" + str(self.y) + ",z=" + str(self.z) + "]"

if __name__ == "__main__":
	print "No testcases";
