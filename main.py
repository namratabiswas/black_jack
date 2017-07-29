import random
from random import randrange
import sys
import string

import curses

from classCard import Card    

# Creates a 52 card deck with ability to deal from deck
from classDeck import Deck

# Player class with name, chips etc.
from classPlayer import Player

from classDealer import Dealer

# Main game class
from classBlackjack import Blackjack

    
def main():
    game = Blackjack()
    game.intro()
    game.playgame()
main()
