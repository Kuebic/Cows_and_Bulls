#dictionary.py
#by Kenei Menning and Scott Hruska

import random

class Dictionary:

    def __init__(self, wordlength):
        self.words= []
        infile = open("words.txt", "r")
        for line in infile:
            word = line.strip()
            if len(word) == wordlength:
                self.words.append(word)
        infile.close()

    def randomWord(self):
        secret = random.choice(self.words)
        self.secret = secret
        return self.secret

    def check(self, word):
        for w in self.words:
            wString = str(w)
            if word == wString.upper():
                return True
            
                
                
