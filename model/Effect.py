__author__ = 'Eshaan'

TYPE_PREFIXES = {0 : "ATSTART", 1 : "CLICK"}
ACTION_PREFIXES = ["GAIN", "LOSE"]
ACTION_SUFFIXES = ["GREEN", "GOLD", "ELECTRIC", "ATTACK"]

def stringToEffect(givenString):
    parts = givenString.split("_")
    effect_type = parts[0]
    action = parts[1]
    return Effect(effect_type, action)

class Effect:

    def __init__(self, effect_type, action):
        self.effect_type = effect_type #click, passive, start, extra cost
        self.action = action #gain something, lose something etc.