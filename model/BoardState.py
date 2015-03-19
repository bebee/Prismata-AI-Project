__author__ = 'Eshaan'


class BoardState:

    p1Turn = True
    p1 = None
    p2 = None

    def __init__(self, p1, p2):
        #game loop
        turnCount = 0
        self.setupBoard()
        while True:
            if p1.hasNoCards() and not p2.hasNoCards():
                #p2 wins
                pass
            elif p2.hasNoCards() and not p1.hasNoCards():
                pass
            else:
                pass
                #tie
            if p1Turn:
                p1.doTurn()
            else:
                p2.doTurn()
            p1Turn = not p1Turn #increment turn
            pass

    def setupBoard(self):
        pass