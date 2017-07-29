


class Dealer:
    def __init__(self):
        self.hand = []
        self.name = "The Dealer"
        self.score = 0
    def getname(self):
        return self.name
    def sethand(self,card):
        self.hand.append(card)
    def gethand(self):
        return self.hand
    def setscore(self):
        self.score = self.score + 1

    def getscore(self):
        return self.score
    def clearhand(self):
        self.hand = []