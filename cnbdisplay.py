#cnbdisplay.py
#by Kenei Menning and Scott Hruska

from graphics import *

class cnbDisplay:

    def __init__(self, win):
        self.attempt = 0
        self.tries = []
        self.images = []
        self.locations = [(3.5, 11),(3.5, 10.4),(3.5, 9.8),(3.5, 9.2),(3.5, 8.6),
                          (3.5, 8), (3.5, 7.4), (3.5, 6.8),(3.5, 6.2),(3.5, 5.6),
                          (7.0, 11),(7.0, 10.4),(7.0, 9.8),(7.0, 9.2),(7.0, 8.6),
                          (7.0, 8), (7.0, 7.4), (7.0, 6.8),(7.0, 6.2),(7.0, 5.6)]
        
        bg = Rectangle(Point(2,11.5), Point(10,5))
        bg.setFill('white')
        bg.draw(win)
        self.win = win

    def addTry(self, word, bulls, cows):
        content = word + "  " + " " + " " + " "
        gx, gy = self.locations[self.attempt]
        guess = Text(Point(gx, gy), content)
        cnbfile = self.choosegif(bulls, cows)
        cnb = Image(Point(gx+1.1, gy), cnbfile)
        cnb.draw(self.win)
        guess.setFace("courier")
        guess.setStyle("bold")
        guess.setSize(16)
        guess.draw(self.win)
        self.tries.append(guess)
        self.images.append(cnb)
        self.attempt = self.attempt + 1

    def clear(self):
        for b in self.tries:
            b.undraw()
        for i in self.images:
            i.undraw()
        self.attempt = 0

    def choosegif(self, b, c):
        if b == 0:
            if c == 0:
                return "b0c0.gif"
            elif c == 1:
                return "c1.gif"
            elif c == 2:
                return "c2.gif"
            elif c == 3:
                return "c3.gif"
            elif c == 4:
                return "c4.gif"
            elif c == 5:
                return "c5.gif"

        elif b == 1:
            if c == 0:
                return "b1.gif"
            elif c == 1:
                return "b1c1.gif"
            elif c == 2:
                return "b1c2.gif"
            elif c == 3:
                return "b1c3.gif"
            elif c == 4:
                return "b1c4.gif"

        elif b == 2:
            if c == 0:
                return "b2.gif"
            elif c == 1:
                return "b2c1.gif"
            elif c == 2:
                return "b2c2.gif"
            elif c == 3:
                return "b2c3.gif"
                
        elif b == 3:
            if c == 0:
                return "b3.gif"
            elif c == 1:
                return "b3c1.gif"
            elif c == 2:
                return "b3c2.gif"

        elif b == 4:
            if c == 0:
                return "b4.gif"
            elif c == 1:
                return "b4c1.gif"

        elif b == 5:
            return "b5.gif"
        
