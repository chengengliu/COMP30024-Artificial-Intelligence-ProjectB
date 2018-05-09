import time
import PlayerFunction as pf
import AIStrategy as Strategy

class Player():
    def __int__(self, color):
        self.board = Board(color)
        self.strategy = aiStrategy()
        self.enemy = self.board.enemy
        self.player = self.board.player
        self.moving = False
        self.turns = 0

    def action(sefl,turns):
        t = time.time()
        if self.turns < 24:
            action = self.strategy.placingPhase(self.board, self.player)
        else:
            action = self.startegy.move(self.board, self.player)
        self.update(action,self.player)
        return action

    def update(self, action, color = None):
        if self.turns < 24:
            self.board.place(color,action)
