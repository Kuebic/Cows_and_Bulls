#WordBox.py
#by Kenei Menning and Scott Hruska

from graphics import *
from button import Button

class Wordbox:

    def __init__(self, win, wordsize):
        self.box = Rectangle(Point(5-wordsize/3, 4.5), Point(5+wordsize/3, 3.75))
        self.box.setFill("White")
        self.box.setWidth(3)
        self.box.draw(win)
        cbox = self.box.getCenter()
        self.word = Text(cbox, "")
        self.word.setFace("courier")
        self.word.setStyle("bold")
        self.word.setSize(26)
        self.word.draw(win)
        self.size = wordsize

    def addLetter(self, ch):
        currentWord = self.word.getText()
        if len(currentWord) < self.size:
            newWord = currentWord+ch
            self.word.setText(newWord)

    def delLetter(self):
        currentWord = self.word.getText()
        self.word.setText(currentWord[:-1])

    def getWord(self):
        return self.word.getText()

    def clear(self):
        self.word.setText("")

    def undraw(self):
        self.word.undraw()
        self.box.undraw()
        
