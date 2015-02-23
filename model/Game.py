__author__ = 'Eshaan'

from Player import Player

class Game:

    def __init__(self, player1, player2, cardList):
        self.player1 = player1
        self.player2 = player2
        self.currPlayer = 1 #p1 starts
        self.cardList = cardList

