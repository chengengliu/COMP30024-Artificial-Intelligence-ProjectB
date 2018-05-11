import math

CORNER  = "X"
EMPTY = "-"
CENTER = 3.5

class Utility:
    '''
    The Utility class is used for selecting the best actions in both moving
        phase and placing phase. Implement key function to make it comparable.
    '''
    def __init__(self,board):
        self.board = board
    #Less than
    def __lt__(self,other):
        if other == -math.inf:
            return False
        elif other == math.inf:
            return True
        return (piecesRemain(self.board),pieceDistance(self.board), fragilePiece(self.board))<(piecesRemain(other.board),pieceDistance(other.board), fragilePiece(other.board))
    #Greater than
    def __gt__(self,other):
        if other == -math.inf:
            return True
        elif other == math.inf:
            return False
        return (piecesRemain(self.board),pieceDistance(self.board), fragilePiece(self.board))>(piecesRemain(other.board),pieceDistance(other.board), fragilePiece(other.board))

    #Greater or equal
    def __ge__(self,other):
        if other == -math.inf:
            return True
        elif other == math.inf:
            return False
        return (piecesRemain(self.board),pieceDistance(self.board), fragilePiece(self.board))>=(piecesRemain(other.board),pieceDistance(other.board), fragilePiece(other.board))
    #Equal
    def __eq__(self,other):
        if other == -math.inf:
            return False
        elif other == math.inf:
            return False
        return (piecesRemain(self.board),pieceDistance(self.board), fragilePiece(self.board))==(piecesRemain(other.board),pieceDistance(other.board), fragilePiece(other.board))
    #Not equal
    def __ne__(self,other):
        if other == -math.inf:
            return True
        elif other == math.inf:
            return True
        return (piecesRemain(self.board),pieceDistance(self.board), fragilePiece(self.board))!=(piecesRemain(other.board),pieceDistance(other.board), fragilePiece(other.board))
    #Less or equal
    def __le__(self,other):
        if other == -math.inf:
            return False
        elif other == math.inf:
            return True
        return (piecesRemain(self.board),pieceDistance(self.board), fragilePiece(self.board))<=(piecesRemain(other.board),pieceDistance(other.board), fragilePiece(other.board))

def pieceDistance(board):
    '''
    param: board
    function: calculate average distance from center to each of a type of color.
        (given a particular board state). The piece should move towards the center
        and reduce the distance.
    return: inverse of average distance.
    '''
    distance = 0
    pieceNum = 0
    for column in range(len(board.grid)):
        for row in range(len(board.grid[column])):
            piece = board.grid[column][row]
            if piece == board.player:
                pieceNum+=1
                distance+=math.sqrt((abs(column-CENTER)**2)+(abs(row-CENTER)**2))

    distance/= pieceNum
    return -distance

def piecesRemain(board):
    '''
    param: board
    function: calculate the difference between player piece and opponent piece
    return: the difference
    '''
    return board.playerPieces - board.opponentPieces

def fragilePiece(board):
    '''
    param: board
    function: calculate total fragileness of a given type of piece(under a
        particular board state). This fragileness indicates how easily one piece
        can be eliminated. Yet basically that should be avoided.
    return: inverse of fragileness
    '''
    fragile = 0
    for column in range(len(board.grid)):
        for row in range(len(board.grid[column])):
            piece = board.grid[column][row]
            if piece == board.player:
                try:
                    #Check left and right.
                    left = board.grid[column-1][row]
                    right = board.grid[column+1][row]
                    #If right has opponent or corner and left is empty
                    if (right==board.opponent or right == CORNER) and (left==EMPTY) and (column-1>=0):
                        fragile+=1
                    #If left has opponent or corner and right is empty
                    if (left==board.opponent or left == CORNER) and (right==EMPTY) and (column+1 <=7):
                        fragile+=1
                except:
                    pass
                try:
                    #Check up and down
                    down = board.grid[column][row+1]
                    up = board.grid[column][row-1]
                    #If down has opponent or corner and up is empty
                    if (down==board.opponent or down == CORNER) and (up==EMPTY) and(row-1>=0):
                        fragile+=1
                    #If up has opponent or corner and down is empty
                    if (up==board.opponent or up == CORNER) and (down==EMPTY) and (row+1<=7):
                        fragile+=1
                except:
                    pass
    return -fragile
