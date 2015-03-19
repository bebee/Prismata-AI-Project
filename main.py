import json
from model.Card import JsonToCard
from model.BoardState import BoardState
from model.Player import Player

__author__ = 'Eshaan'

#TODO install wireshark and try to get json from there or something similar

cardsFile = open("cards.txt")

cardMap = json.loads(cardsFile.read())['cards'];

cardList = []

for card in cardMap:
    cardList.append(JsonToCard(card))

p1Cards = []


player1 = Player(p1Cards)
player2 = Player()

mBoardState = BoardState()

