class Card:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["2","3","4","5","6","7","8","9","Ten","Jack","Queen","King","Ace"]
    def __init__(self, value, suit):
        self.value, self.suit = value, suit
    def __str__(self):
        return self.values[self.value] + " of " + self.suits[self.suit] 