import math
from copy import deepcopy
from AIBoard import Board
from UtilityFunction import Utility
DEPTH = 5 # we have tested different depth to find the most effiecent one that
          # could get the job done without taking too much time and space

class Strategy:
    '''
    The Strategy class can do MinMax/AlphBeta pruning and select the best action
    to perform moving phase and placing phase
    '''
    def __init__(self):
        pass
    def placingPhase(self,board, color):
        '''
        param: board, color
        function: call MinMax and generate a list of actions. Select the best
            one and return.
        return: action(tuple)
        '''
        placingList = []
        for places in board.possiblePlacing(color):
            #Make a copy as we don't want to change the board.
            #Several movements are "made" and the best will be selected
            copyOfBoard = deepcopy(board)
            copyOfBoard.place(color, places)
            placingList.append((self.placingMinMax(copyOfBoard,board.opponent, -math.inf,math.inf,0),places))

        return max(placingList)[1] #Sort the list of possible actions. Return the best one
    def placingMinMax(self,board, color, a, b,depth):
        '''
        param:board, color, alpha, beta, depth
        function: MinMax algorithm used for placing phase.
            Have the alpha-beta pruning algorithm as well.
        return: a comparable object value
        '''
        if depth == 2 or board.playerPieces <= 15:
            return Utility(board)

        if color == board.player:
            value = -math.inf
            # PossiblePlacing will return a (row,column) tuple
            for place in board.possiblePlacing(color):
                copyOfBoard = deepcopy(board)
                copyOfBoard.place(color,place)
                value = max(value,self.placingMinMax(copyOfBoard, board.opponent, a,b,depth+1))
                a = max(a,value)
                # Alpha meets beta, time to prune
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
        param: board, color
        function: call MinMax and generate a list of actions. Select the best
            one and return.
        return: action(tuple)
        '''
        movingList = []
        for move in board.possibleMoves(color):
            #Make a copy as we don't want to change the board.
            #Several movements are "made" and the best will be selected
            copyOfBoard = deepcopy(board)
            #Remember that move is 2 2D tuple contaning "Origin" and "Goal". Two positions
            copyOfBoard.makeMove(color,move[0], move[1])
            movingList.append((self.movingMinMax(copyOfBoard,board.opponent,-math.inf,math.inf,0),move))
        return max(movingList)[1] #Sort based on Utility. Return the best move

    def movingMinMax(self,board, color, a,b,depth):
        '''
        param:board, color, alpha, beta, depth
        function: MinMax algorithm used for placing phase.
            Have the alpha-beta pruning algorithm as well.
        return: a comparable object value
        '''
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
                # Alpha meets beta, time to prune
                if b <= a:
                    break
            return value
        else:
            value = math.inf
            for move in board.possibleMoves(color):
                # copy board to prevent changing the actual game board while
                # just checking available move space
                copyOfBoard = deepcopy(board)
                copyOfBoard.makeMove(color,move[0], move[1])
                value = min(value,self.placingMinMax(copyOfBoard, board.player, a,b,depth+1))
                b = min(b,value)
                # Alpha meets beta, time to prune
                if b<=a:
                    break
            return value
