
import PlayerFunction as pf
from AIStrategy import Strategy
from AIBoard import Board

WHITE = "O"
BLACK = "@"
CORNER = "X"
EMPTY = "-"

class Player:
    def __init__(self, color):

        self.board = Board(color)
        self.strategy = Strategy()
        self.opponent = self.board.opponent
        self.player = self.board.player
        self.turns = 0

    def action(self,turns):
        self.turns+=1
        if self.turns <= 24:
            action = self.strategy.placingPhase(self.board, self.player)
            self.board.place(self.player, action)
        else:
            action = self.strategy.movingPhase(self.board, self.player)
            self.board.makeMove(self.player,action[0], action[1])

        if (turns >128 and turns <192):
            self.board.size = 6
            self.board.shrinkBoard(self.board.numberOfShrink())
        elif (turns >= 192):
            self.board.size = 4
            self.board.shrinkBoard(self.board.numberOfShrink())
        return action

    def update(self, action):
        origin = action[0]
        goal = action[1]
        self.turns+=1
        if self.turns <= 24:
            self.board.place(self.opponent, action)
        else:
            self.board.makeMove(self.opponent,origin,goal)
