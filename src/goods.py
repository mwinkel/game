__author__="Yves Adler"
__date__ ="$Nov 5, 2009 3:10:01 PM$"

if __name__ == "__main__":
	print "Testcases here?";


class Goods(object):
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
	def __init__(self):
		print "Stamm erstellt"

class Plank(Goods):
	pass

class Stone(Goods):
	pass