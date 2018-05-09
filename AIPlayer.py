import time
from AIStrategy import aiStrategy
class Player():
    def __int__(self, color):
        self.board = Board(color)
        self.strategy = aiStrategy()
        self.enemy = self.board.enemy
        self.player = self.board.player
        self.moving = False
