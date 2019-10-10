#Bulls and Cows Phase 1
#by Kenei Menning and Scott Hruska

from graphics import *
from button import *
from wordbox import Wordbox
from cnbdisplay import cnbDisplay
from dictionary import *
from cnbsecret import *
import time

class CnBGame:

    def __init__(self):
        win = GraphWin("Cows and Bulls", 600, 600)
        win.setCoords(0,0,12,12)
        win.setBackground("slategray")
        self.win = win
        self.wordlength = 4
        self.word = Wordbox(win, self.wordlength)
        self.__createButtons()
        display = cnbDisplay(win)
        self.display = display
        self.dict = Dictionary(self.wordlength)
        self.sec = self.dict.randomWord()
        self.secret = CnBSecret(self.sec)
        self.message = Text(Point(9.5,4.25), "")
        self.message.draw(self.win)
        self.message.setFace("courier")
        self.message.setStyle("bold")
        logo = Image(Point(6,11.6), "cnb.gif")
        logo.draw(win)

    def __createButtons(self):
        bSpecs = [(1,3,"Q"), (2,3,"W"),(3,3,"E"),(4,3,"R"),(5,3,"T"),(6,3,"Y"),(7,3,"U"),(8,3,"I"),(9,3,"O"),(10,3,"P"),
                  (1.5,2,"A"),(2.5,2,"S"),(3.5,2,"D"),(4.5,2,"F"),(5.5,2,"G"),(6.5,2,"H"),(7.5,2,"J"),(8.5,2,"K"),(9.5,2,"L"),
                  (2,1,"Z"),(3,1,"X"),(4,1,"C"),(5,1,"V"),(6,1,"B"),(7,1,"N"),(8,1,"M")]
        bSpecs2 = [(1,11,"New"),(1,10,"Quit"), (1,4.5,"Peek")]
        self.buttons=[]
        for (cx,cy,label) in bSpecs:
            self.buttons.append(Button(self.win,Point(cx,cy),.75,.75,label))
        for (cx,cy,label) in bSpecs2:
            self.buttons.append(Button(self.win,Point(cx,cy),1.5,1,label))
        self.buttons.append(Button(self.win, Point(10.75,2), 1.5, .75, "Try"))
        self.buttons.append(Button(self.win, Point(10,1), 1.5, .75, "BKSP"))
        for b in self.buttons:
            b.activate()
        
        
    def getButtonPress(self):
        while True:
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel()
                
    def run(self):
        while True:
            b = theGame.getButtonPress()
            
            if b == "Quit":
                self.win.close()
                break
            
            elif b == "BKSP":
                self.word.delLetter()
                
            elif b == "Try":
                theGame.doTry()
                
            elif b == "New":
                theGame.doNew()

            elif b == "Peek":
                message = "The word was: {0} ".format(self.secret.getSecret())
                self.message.setText(message)
                while True:
                    b = theGame.getButtonPress()
                    if b == "Quit":
                        self.win.close()
                        break
                    elif b == "New":
                        theGame.doNew()
                        break
                
            else:
                self.word.addLetter(b)

    def doTry(self):
        attempt = self.word.getWord()
        attemptString = str(attempt)
        if len(attempt) != self.wordlength:
            self.message.setText("Input is too short")
                
        elif self.dict.check(attemptString) != True:
            self.message.setText("Input is not a word")
            
        elif self.dict.check(attemptString) == True:
            b, c = self.secret.checkGuess(attemptString)
            self.display.addTry(attempt,b,c)
            self.message.setText("")
            self.word.clear()
            lose = self.secret.getCount()
            if b == self.wordlength:
                self.message.setText("YOU WON!!! OMGWTFBBQ!!!")
                f1 = Image(Point(3,4), "f1.gif")
                f2 = Image(Point(9,8), "f2.gif")
                f3 = Image(Point(6,5), "f3.gif")
                won = Image(Point(6,8), "You-Won.gif")

                for i in range(8):
                    won.draw(self.win)                    
                    f1.draw(self.win)
                    time.sleep(.1)
                    
                    f1.undraw()
                    f1.move(5,5)
                    time.sleep(.04)
                    
                    f2.draw(self.win)
                    time.sleep(.1)
                    
                    f2.undraw()
                    f2.move(-6, -1)
                    won.undraw()
                    time.sleep(.04)
                    
                    f3.draw(self.win)
                    time.sleep(.1)
                    
                    f3.undraw()
                    f3.move(2, -3)
                    time.sleep(.04)

                    won.draw(self.win)
                    f1.draw(self.win)
                    time.sleep(.1)

                    f1.undraw()
                    f1.move(-5,-5)
                    time.sleep(.04)

                    f2.draw(self.win)
                    time.sleep(.1)
                    
                    f2.undraw()
                    f2.move(6, 1)
                    won.undraw()
                    time.sleep(.04)

                    f3.draw(self.win)
                    time.sleep(.1)
                    
                    f3.undraw()
                    f3.move(-2, 3)
                    time.sleep(.04)
                    
                while True:
                    b = theGame.getButtonPress()
                    if b == "Quit":
                        self.win.close()
                        break
                    elif b == "New":
                        theGame.doNew()
                        break
            
            elif lose == 20:
                message = "You Lost.  The word was: {0} ".format(self.secret.getSecret())
                self.message.setText(message)
                lost = Image(Point(6,8), "You-Lost.gif")
                meat = Image(Point(6,3), "ham1.gif")

                for i in range(10):
                    lost.draw(self.win)
                    meat.draw(self.win)
                    time.sleep(.5)
                    f1.undraw()
                    time.sleep(.5)
                meat.undraw()
                    
                while True:
                    b = theGame.getButtonPress()
                    if b == "Quit":
                        self.win.close()
                        break
                    elif b == "New":
                        theGame.doNew()
                        break
        
            

    def doNew(self):
        window = GraphWin("New Game", 200, 200)
        window.setBackground("slategray")
        window.setCoords(0,0,4,4)
        but1 = Button(window, Point(1,1.5), 1, 1, "3")
        but2 = Button(window, Point(2,1.5), 1, 1, "4")
        but3 = Button(window, Point(3,1.5), 1, 1, "5")
        but1.activate()
        but2.activate()
        but3.activate()
        instructions = Text(Point(2, 2.5), "Choose Word Length")
        instructions.draw(window)
        self.message.setText("")
        while True:
            click = window.getMouse()
            if but1.clicked(click):
                self.wordlength = 3
                break
            if but2.clicked(click):
                self.wordlength = 4
                break
            if but3.clicked(click):
                self.wordlength = 5
                break
        self.dict = Dictionary(self.wordlength)
        self.sec = self.dict.randomWord()
        self.secret = CnBSecret(self.sec)
        self.word.undraw()
        self.word = Wordbox(self.win, self.wordlength)
        self.display.clear()
        window.close()


        

if __name__ == '__main__':
    theGame = CnBGame()
    theGame.run()
            
