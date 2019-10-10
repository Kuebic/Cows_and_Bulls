#cnbsecret.py
#by Kenei Menning and Scott Hruska

class CnBSecret:

    def __init__(self, word):
        self.secret = word
        self.count = 0

    def checkGuess(self, guess):
        self.count = self.count + 1
        

        bulls = 0
        cows = 0
        guessList = list(guess.lower())
        wordList = list(self.secret)
        
        for pos in range(len(guess)):
            if guessList[pos] == wordList[pos]:
                bulls = bulls + 1
                guessList[pos] = "&"
                wordList[pos] = "$"
                
        for pos in range(len(guess)):
            letter = guessList[pos]
            wordString = "".join(wordList)
            if wordString.find(letter) >= 0:
                position = wordString.find(letter)
                wordList[position] = "$"
                guessList[pos] = "&"
                cows = cows + 1
                        
        return bulls, cows
        

    def length(self):
        return len(self.secret)

    def getCount(self):
        return self.count

    def getSecret(self):
        return self.secret
