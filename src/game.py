import goods
import buildings
import game
from buildings import people
import pygame

__author__="Yves Adler"
__date__ ="$Nov 5, 2009 3:10:01 PM$"


class Game(object):
	""" the big mama, aye? """

	def __init_pygame__(self):
		pygame.init()
		self._clock = pygame.time.Clock()

	def __init__(self):
		self.__init_pygame__()
		self._ticks = 0.0
		self._buildings = []
		self._people = []
		self._goods = []

	def run(self):
		""" start game """
		while True:
			# Limit frame speed to 50 FPS
			self._ticks += self._clock.tick(50)
#			print self._ticks

			inventory = self._goods # should be something liek create_inventory() which counts whats around in the warehouses!
			self.create_requirement_dict()
			for building in self._buildings:
				building.work(self._ticks)
			

	def create_requirement_dict(self):
		transport = dict()

		for building in self._buildings:
			if building.requires_goods():
				transport[building] = building.requires_goods()

		return transport
	
	def add_building(self, building):
		self._buildings.append(building)

	def tick(self, time):
		""" main gameloop """
		pass
		



if __name__ == "__main__":
	print "-- ein kleiner spiel mit siedlern v0.000001 --"
	game = Game()
	game.add_building(buildings.LumberjackHouse())
	game.add_building(buildings.LumberjackHouse())
	game._goods = [goods.Plank(), goods.Plank(), goods.Stone(), goods.Stone()] # ugly hack!
	game._people = [people.Flattener(), people.Builder(), people.Lumberjack()]
#	game.run()
	print game.create_requirement_dict()
	print "-fin-"