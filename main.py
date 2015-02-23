import json
from model import Card
from model.Card import JsonToCard

__author__ = 'Eshaan'


cardsFile = open("cards.txt")

cardMap = json.loads(cardsFile.read())['cards'];

cardList = []

for card in cardMap:
    cardList.append(JsonToCard(card))

for card in cardList:
    print(str(card))