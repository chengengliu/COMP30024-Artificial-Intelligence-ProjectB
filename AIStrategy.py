import math
import Utility
from copy import deepcopy
import AIBoard as Board

class Strategy:
    def __int__(self):
        pass
    def placingPhase(self,board, color):
        copyOfBoard = []
        copyOfBoard = deepcopy(board)
        copyOfBoard.place(color, placingPhase)
        #copyOfBoard.append()
    def placingMinMax(self,board, color, a, b):
        pass


    def movingPhase(self,board, color):
        copyOfBoard = []
        #copyOfBoard = deepcopy(board)
        #copyOfBoard.makeMove()
        for move in 
