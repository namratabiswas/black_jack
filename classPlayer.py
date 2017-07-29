


class Player:
    def __init__(self, name = "Player"):
        self.hand = []
        self.name = name
        self.chips = 100
        self.score = 0
    def getchips(self):
        return self.chips
    def sethand(self, card):
        self.hand.append(card)
    def gethand(self):
        return self.hand
    def setchips(self, add):
        self.chips = self.chips + add
    def setname(self):
        self.name = raw_input("What is your name? ")
    def getname(self):
        return self.name
    def setscore(self):
        self.score = self.score + 1
    def getscore(self):
        return self.score
    def clearhand(self):
        self.hand = []