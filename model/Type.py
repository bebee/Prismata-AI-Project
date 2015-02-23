__author__ = 'Eshaan'

class Type:

    CLICK = "click"
    AT_START = "atstart"
    ONE_TIME = "one_time"
    EXTRA_COST = "extra_cost"

    def __init__(self, type):
        self.type = type

    def get(self):
        return self.type

    def equals(self, type):
        return type == self.type