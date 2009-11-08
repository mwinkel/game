# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="Yves Adler"
__date__ ="$Nov 7, 2009 8:00:32 PM$"

from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
from pygame.locals import * # events und co


class PyGfxEngine:

	def __init__(self):
		self._running = True

		pygame.init()
		pygame.display.set_caption('PyGfxEngine Test')
		screen_size = (640,480)
		self._window = pygame.display.set_mode(screen_size, OPENGL|DOUBLEBUF)

		self.__init_opengl()
		self.__resize_window(screen_size)


	def __del__(self):
		pygame.quit()

	def __init_opengl(self):
		# TODO: was ist wirklich benoetigt?
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
		glEnable(GL_TEXTURE_2D)
		glShadeModel(GL_SMOOTH)
		glClearColor(0.5, 0.5, 0.5, 0.0)
		glClearDepth(1.0)
		glPointSize(5)
		glEnable(GL_DEPTH_TEST)
		glEnable(GL_ALPHA_TEST)
		glDepthFunc(GL_LEQUAL)
		glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
		glAlphaFunc(GL_NOTEQUAL,0.0)

	def __resize_window(self, (width, height)):
		# TODO: wie kann man das nu dynamisch resizen?
		glViewport(0, 0, width, height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(45, 1.0*width/height, 0.1, 1000.0)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

	def input(self, events):
		for event in events:

			if event.type == QUIT:
				self._running = False
				break
			else:
				print event


	def draw_point(self, x, y, z):
		glTranslatef(x,y,z)
		glBegin(GL_POINTS)
		glVertex3f(0,0,0)
		glEnd()
		glLoadIdentity()

	def draw(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()
		
		glColor3f(0,1,0)
		self.draw_point(-1, 0, -6)

		glColor3f(0,1,1)
		self.draw_point(1, 0, -6)

		#Draw on Screen
		
		pygame.display.flip()

	def run(self):
		""" main eninge loop """
		while self._running:

			self.input(pygame.event.get())
			self.draw()


if __name__ == "__main__":
	engine = PyGfxEngine()
	engine.run()
