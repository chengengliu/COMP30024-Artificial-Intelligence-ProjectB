import math
CORNER  = "X"
EMPTY = "-"
CENTER = 3.5
class Utility:
    def __init__(self,board):
        self.board = board

    def __lt__(self,other):
        if other == -math.inf:
            return False
        elif other == math.inf:
            return True
        return (piecesRemain(self.board),pieceDensity(self.board), fragilePiece(self.board))<(piecesRemain(other.board),pieceDensity(other.board), fragilePiece(other.board))
    def __gt__(self,other):
        if other == -math.inf:
            return True
        elif other == math.inf:
            return False
        return (piecesRemain(self.board),pieceDensity(self.board), fragilePiece(self.board))>(piecesRemain(other.board),pieceDensity(other.board), fragilePiece(other.board))

    def __ge__(self,other):
        if other == -math.inf:
            return True
        elif other == math.inf:
            return False
        return (piecesRemain(self.board),pieceDensity(self.board), fragilePiece(self.board))>=(piecesRemain(other.board),pieceDensity(other.board), fragilePiece(other.board))

    def __eq__(self,other):
        if other == -math.inf:
            return False
        elif other == math.inf:
            return False
        return (piecesRemain(self.board),pieceDensity(self.board), fragilePiece(self.board))==(piecesRemain(other.board),pieceDensity(other.board), fragilePiece(other.board))
    def __ne__(self,other):
        if other == -math.inf:
            return True
        elif other == math.inf:
            return True
        return (piecesRemain(self.board),pieceDensity(self.board), fragilePiece(self.board))!=(piecesRemain(other.board),pieceDensity(other.board), fragilePiece(other.board))

    def __le__(self,other):
        if other == -math.inf:
            return False
        elif other == math.inf:
            return True
        return (piecesRemain(self.board),pieceDensity(self.board), fragilePiece(self.board))<=(piecesRemain(other.board),pieceDensity(other.board), fragilePiece(other.board))



def piecesRemain(board):
    return board.playerPieces - board.opponentPieces

def pieceDensity(board):
    distance = 0
    pieceNum = 0
    for column in range(len(board.grid)):
        for row in range(len(board.grid[column])):
            piece = board.grid[column][row]
            if piece == board.player:
                pieceNum+=1
                distance+=math.sqrt((abs(column-CENTER)**2)+(abs(row-CENTER)**2))
    if pieceNum ==0:
        return 0
    else:
        distance/= pieceNum
        return -distance

def fragilePiece(board):
    fragile = 0
    for column in range(len(board.grid)):
        for row in range(len(board.grid[column])):
            piece = board.grid[column][row]
            if piece == board.player:
                try:
                    #Check left and right.
                    left = board.grid[column-1][row]
                    right = board.grid[column+1][row]
                    if (right==board.opponent or right == CORNER) and (left==EMPTY) and (column-1>=0):
                        fragile+=1
                    if (left==board.opponent or left == CORNER) and (right==EMPTY) and (column+1 <=7):
                        fragile+=1
                except:
                    pass
                try:
                    #Check up and down
                    down = board.grid[column][row+1]
                    up = board.grid[column][row-1]
                    if (down==board.opponent or down == CORNER) and (up==EMPTY) and(row-1>=0):
                        fragile+=1
                    if (up==board.opponent or up == CORNER) and (down==EMPTY) and (row+1<=7):
                        fragile+=1
                except:
                    pass
    return -fragile
