import random
from random import randrange
from classCard import Card
class Deck:
    def __init__(self):
        self.cards = []
        for x in range(13):
            for y in range(4):
                self.cards.append(Card(x, y))
    def __str__(self):
        return self.cards
    def deal(self, handsize):
        dealtcards = []
        for i in range(handsize):
            dealtcards.append(str(self.cards[randrange(52)]))
        return dealtcards
    def printdeck(self):
        for card in self.cards:
            print card