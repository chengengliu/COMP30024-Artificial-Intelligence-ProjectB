from Board import Board
from AlphaBeta import AlphaBeta
from Strategy import Strategy

class Player:

    def __init__(self, color):
        self.color = color
        self.board = Board()
        if(self.color == 'white'):
            self.oppColor = 'black'
        else:
            self.oppColor = 'white'
    
    def actions(self, turns):
        self.turns = turns
        # self.board.updateBoard(self.playerAction, self.color)

    def update(self, action):
        self.action = action
        self.board.updateBoard(self.action, self.oppColor)
