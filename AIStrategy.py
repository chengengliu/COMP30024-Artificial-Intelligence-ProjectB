import math
import Utility
from copy import deepcopy
import PlayerFunction as pf

from AIBoard import Board

class Strategy:
    def __init__(self):
        pass
    def placingPhase(self,board, color):
        '''
        Placing phase for the player
        '''
        copyOfBoards = []
        #copyOfBoard = deepcopy(board)
        for place in board.possiblePlacing(color):
            copyOfBoard = deepcopy(board)
            copyOfBoard.place(color, place)
            #print("!!!!!!!!!!")
            copyOfBoards.append(self.placingMinMax(copyOfBoard,board.opponent, -math.inf,math.inf,0))
        #print(max(copyOfBoards)[1])
        print("Hello")
        return max(copyOfBoards)[1]

        #copyOfBoard.place(color, )
        #copyOfBoard.append()
    def placingMinMax(self,board, color, a, b,depth):
        '''
        MinMax algorithm used for placing phase.
        Have the alpha-beta pruning algorithm as well.
        a: alpha
        b: beta

        还有一个问题： 如何解决当最后剩余棋子两个？四个？很少的时候
        而且如何解决 深度问题 depth不能太深。 当深度超过一定范围时候，是否应该跳出
        MinMax搜索以避免memory不足？

        '''
        #print("Hello")
        if color == board.player:
            value = -math.inf
            # PossiblePlacing will return a (row,column) tuple
            for place in board.possiblePlacing(color):
                copyOfBoard = deepcopy(board)
                copyOfBoard.place(color,place)
                value = max(value,self.placingMinMax(copyOfBoard, board.opponent, a,b,depth+1))
                a = max(a,value)
                if b <= a:
                    break
            return value
        else:
            value = math.inf
            for place in board.possiblePlacing(color):
                copyOfBoard = deepcopy(board)
                copyOfBoard.place(color,place)
                value = min(value,self.placingMinMax(copyOfBoard, board.opponent, a,b,depth+1))
                b = min(b,value)
                if b<=a:
                    break
            return value

    def movingPhase(self,board, color):
        '''
        Moving phase for the player
        '''
        copyOfBoard = []
        #copyOfBoard = deepcopy(board)
        #copyOfBoard.makeMove()
        for move in board.possibleMoves(color):
            copyOfBoard = deepcopy(board)
            copyOfBoard.makeMove()


    def movingMinMax(self,board, color, a,b,depth):
        pass
