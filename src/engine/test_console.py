__author__="Marcel Winkel"
__date__ ="$Nov 8, 2009 10:40:53 AM$"

class Console:
        def __init__(self, screen):
                self.screen = screen
                self.screensize = self.screen.get_size()
                self.screenwidth = self.screensize[0]
                self.screenheight = self.screensize[1]

                self.text = 'opengl console - testing\n'

                self.active = False

        def __str__(self):
                return self.text + str(self.screenwidth) + 'x' + str(self.screenheight)

        def set_active(self, force=None):
                if not force:
                        self.active = not self.active
                else:
                        self.active = force

#if __name__ == "__main__":
#        print "opengl console testing";

