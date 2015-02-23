from itertools import izip_longest

__author__ = 'Eshaan'


def __grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)


def stringToCost(costString):
    returnCost = Cost()
    for group in __grouper(costString, 2):
        count = int(group[0])
        type = group[1].lower()
        returnCost.attributeMap[type](returnCost, count)
    return returnCost

class Cost:

    def __init__(self, green=None, blue=None, red=None, gold=None, electric=None):
        self._green = green
        self._blue = blue
        self._red = red
        self._gold = gold
        self._electric = electric

    def setGreen(self, green):
        self._green = green

    def setRed(self, red):
        self._red = red

    def setBlue(self, blue):
        self._blue = blue

    def setGold(self, gold):
        self._gold = gold

    def setElectric(self, electric):
        self._electric = electric

    def __str__(self):
        return "green: {!s} blue: {!s} red: {!s} gold: {!s} electric: {!s}".format(self._green,
                    self._blue, self._red, self._gold, self._electric)

    attributeMap = {"g" : setGreen, "b" : setBlue, "r" : setRed, "o" : setGold, "e" : setElectric}

