WHITE = "O"
BLACK = "@"
CORNER = "X"
EMPTY = "-"
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
            #print("Hello")
        else:
            action = self.startegy.moving(self.board, self.player)
        #self.update(action,self.player)
        #print(action)
        print("Action is ", action)
        self.board.place(self.player, action)
        return action

    def update(self, action):
        origin = action[0]
        goal = action[1]
        #print("World")
        self.turns+=1

        if self.turns < 24:
            self.board.place(self.opponent, action)
        else:
            #print("wrodl")
            self.board.makeMove(self.opponent,origin,goal)



        '''
        if self.turns < 24:
            self.board.place(color,action)'''

#player = Player("white")
