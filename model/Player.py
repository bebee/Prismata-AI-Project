from model import Card

__author__ = 'Eshaan'

def populateCardList(p1Or2, cardList):
    droneCount = 8 if p1Or2 else 10
    engiCount = 2
    for card in cardList:
        if card.name == Card.DRONE:
            for i in xrange(droneCount):
                cardList.append(card)
        if card.name == Card.ENGINEER:
            for i in xrange(engiCount):
                cardList.append(card)

class Player:

    def __init(self, myCards, persistentResources, nonPersistentResources):
        self.myCards = myCards
        self.persistentResources = persistentResources
        self.nonPersistentResources = nonPersistentResources
