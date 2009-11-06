__author__="Yves Adler"
__date__ ="$Nov 5, 2009 3:10:01 PM$"

import buildings

class Position(object):
	def __init__(self):
		self.x = 0.0
		self.y = 0.0
		self.z = 0.0



class GameManager(object):
	""" the big mama, aye? """

	def __init__(self):
		pass



if __name__ == "__main__":
	print "-- ein kleiner spiel mit siedlern v0.000001 --"
	b = buildings.Lumberjack
	print dir(b)
