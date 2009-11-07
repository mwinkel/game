from gameobject import *

__author__="Yves Adler"
__date__ ="$Nov 5, 2009 3:10:01 PM$"


class Goods(Gameobject):
	""" Base class for all goods """
	pass

##########################################

class Resource(Goods):
	""" Base class for all 'natural' resources """
	pass

class Tree(Resource):
	pass

class Granite(Resource):
	pass

##########################################

class Wood(Goods):
	pass

class Plank(Goods):
	pass

class Stone(Goods):
	pass


if __name__ == "__main__":
	print "Testcases here?";
