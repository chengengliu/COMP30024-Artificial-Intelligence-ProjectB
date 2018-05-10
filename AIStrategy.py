import math
import Utility
from copy import deepcopy
import PlayerFunction as pf

from AIBoard import Board
#from Utility import Utility
from UtilityFunction import Utility

class Strategy:
    def __init__(self):
        pass
    def placingPhase(self,board, color):
        '''
        Placing phase for the player
        '''
        placingList = []

        for places in board.possiblePlacing(color):
            copyOfBoard = deepcopy(board)
            copyOfBoard.place(color, places)
            placingList.append((self.placingMinMax(copyOfBoard,board.opponent, -math.inf,math.inf,0),places))

        return max(placingList)[1] #Sort the list of possible actions. Return the best one
    def placingMinMax(self,board, color, a, b,depth):
        '''
        MinMax algorithm used for placing phase.
        Have the alpha-beta pruning algorithm as well.
        a: alpha
        b: beta
        '''
        if depth == 2 or board.playerPieces <= 12:
            return Utility(board)

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
                value = min(value,self.placingMinMax(copyOfBoard, board.player, a,b,depth+1))
                b = min(b,value)
                if b<=a:
                    break
            return value

    def movingPhase(self,board, color):
        '''
        Moving phase for the player
        '''
        movingList = []
        #print("HELLLLLLLLO")
        for move in board.possibleMoves(color):
            #Remember that move is 2 2D tuple contaning "Origin" and "Goal". Two positions
            copyOfBoard = deepcopy(board)
            copyOfBoard.makeMove(color,move[0], move[1])
            movingList.append((self.movingMinMax(copyOfBoard,board.opponent,-math.inf,math.inf,0),move))
        #print("HEEEALDALJBSDAJLS")
        print(max(movingList)[1])

        return max(movingList)[1] #Sort based on Utility. Return the best move

    def movingMinMax(self,board, color, a,b,depth):
        if depth == 2 or board.playerPieces <= 5:
            return Utility(board)

        if color == board.player:
            value = -math.inf
            # PossiblePlacing will return a (row,column) tuple
            for move in board.possibleMoves(color):
                copyOfBoard = deepcopy(board)
                copyOfBoard.makeMove(color, move[0], move[1])
                value = max(value,self.placingMinMax(copyOfBoard, board.opponent, a,b,depth+1))
                a = max(a,value)
                if b <= a:
                    break
            return value
        else:
            value = math.inf
            for move in board.possibleMoves(color):
                copyOfBoard = deepcopy(board)
                copyOfBoard.makeMove(color,move[0], move[1])
                value = min(value,self.placingMinMax(copyOfBoard, board.player, a,b,depth+1))
                b = min(b,value)
                if b<=a:
                    break
            return value
