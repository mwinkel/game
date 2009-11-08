import pygame
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="Marcel Winkel"
__date__ ="$Nov 8, 2009 10:40:53 AM$"


class Console:
        def __init__(self, screen, rect):

                self.screen = screen
                self.rect = pygame.Rect(rect)
                self.size = self.rect.size

                self.text = "console test"
                self.active = True

                self.bg_color = 0, 0, 0
                self.txt_color = 255, 255, 255
                self.bg_alpha = 255

                self.bg_layer = pygame.Surface(self.size)
		self.bg_layer.set_alpha(self.bg_alpha)
                
                self.txt_layer = pygame.Surface(self.size)
		self.txt_layer.set_colorkey(self.bg_color)

                self.font = pygame.font.SysFont("monospace", 14)


        def c_out(self, text):
                if not str(text):
                        return;

                for line in text:
                        self.text.append(line)

        def activate(self, force=None):
                if not force:
                        self.active = not self.active
                        print 'activate console'
                else:
                        self.active = force

        def draw(self):
                if not self.active:
                        return;
                else:
                        self.txt_layer.fill(self.bg_color)
                        y = 1

                        for line in self.text:
                                tmp = self.font.render(line, True, self.txt_color)
                                self.txt_layer.blit(tmp, (1, y, 0, 0))
                                y += 10

                        tmp = self.font.render(self.text, True, self.txt_color)
                        self.txt_layer.blit(tmp, (1, self.size[1] - 10, 0, 0))
                        self.bg_layer.fill(self.bg_color)
                        self.bg_layer.blit(self.txt_layer, (0,0,0,0))

                        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 1)
                        self.screen.blit(self.bg_layer, self.rect)


if __name__ == "__main__":
        print "console";