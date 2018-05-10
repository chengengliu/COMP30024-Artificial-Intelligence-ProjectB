import PlayerFunction as pf
from AIStrategy import Strategy

from AIBoard import Board

class Player:
    def __init__(self, color):
        self.board = Board(color)
        self.strategy = Strategy()
        self.opponent = self.board.opponent
        self.player = self.board.player
        self.moving = False
        self.turns = 0

    def action(self,turns):
        if self.turns < 24:
            action = self.strategy.placingPhase(self.board, self.player)
            print("Hello")
        else:
            action = self.startegy.moving(self.board, self.player)
        self.update(action,self.player)
        return action

    def update(self, action):
        if self.turns < 24:
            self.board.place(color,action)
player = Player("white")
