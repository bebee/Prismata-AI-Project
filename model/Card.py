from model import Cost

__author__ = 'Eshaan'


def JsonToCard(strJson):
    return Card(
        strJson['name'],
        Cost.stringToCost(strJson["cost"]),
        strJson['effects'],
        strJson['health'],
        "persistent",
        strJson["isblocker"],
        True
    )

class Card:

    HEALTH_REGAINABLE = "health_regainable"
    HEALTH_NOT_REGAINABLE = "health_not_regainable"

    def __init__(self, name, cost, effectList, health, healthType, canBlock, isClickable):
        self.cost = cost
        self.effectList = effectList
        self.health = health
        self.healthType = healthType
        self.isClickable = isClickable
        self.isClicked = False
        self.name = name
        self.canBlock = canBlock

    def __str__(self):
        return ('name: {!s} cost: ({!s}) effectList: {!s} health: {!s} healthType: {!s} canBlock:'
            ' {!s} isClickable: {!s} isClicked: {!s}').format(self.name, str(self.cost), self.effectList,
                self.health, self.healthType, self.canBlock, self.isClickable, self.isClicked)