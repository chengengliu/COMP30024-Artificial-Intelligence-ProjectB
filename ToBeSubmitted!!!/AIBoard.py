from random import shuffle

WHITE = "O"
BLACK = "@"
CORNER = "X"
EMPTY = "-"
INITIAL = 8
class Board:
    '''
    initiate board class with necessary attributes
    '''
    def __init__(self,color):
        if color == 'white':
            color = WHITE
        else:
            color = BLACK
        self.player = color
        self.playerPieces = 0
        self.opponentPieces = 0
        self.size = INITIAL
        self.grid = boardInit()
        self.opponent = getOpponent(color)

    def update(self,color):
        '''
        adding eliminate check function to help with placing and moving phase
        constantly monitoring on how many chess pieces have left on the board
        to help with technics
        '''
        self.eliminate(color)
        opponent = getOpponent(color)
        self.eliminate(opponent)
        numberOfPlayer, numberOfOpponent = 0,0
        for column in range(len(self.grid)):
            for row in range(len(self.grid[column])):
                p = self.grid[column][row]
                if(p == self.player):
                    numberOfPlayer+=1
                if(p == self.opponent):
                    numberOfOpponent+=1

        self.playerPieces = numberOfPlayer
        self.opponentPieces = numberOfOpponent
    def place(self,color, position):
        '''
        Used for placing piece.
        Call update, since every time place a piece, you need to check
        if it can eliminate other pieces.
        '''
        column = position[1]
        row = position[0]
        self.grid[column][row] = color
        self.update(color)

    def makeMove(self, color, origin, goal):
        '''
        Make move from an original point to a goal point.
        It is called after it being checked as it is proper to move.
        # makeMove call update
        '''
        columnFrom = origin[1]
        rowFrom = origin[0]
        columnTo = goal[1]
        rowTo = goal[0]
        #update the board
        self.grid[columnFrom][rowFrom] = "-"
        self.grid[columnTo][rowTo] = color
        self.update(color)

    def possiblePlacing(self,color):
        '''
        Return a list of possible placing phase
        '''
        places = []
        #Possible placing range of different colors
        if color == WHITE:
            min,max = 0,5
        if color == BLACK:
            min,max = 2,7

        for column in range(min,max+1):
            for row in range(len(self.grid[column])):
                if(self.grid[column][row] == "-"): # If empty
                    places.append((row,column)) #row column 的tuple
        shuffle(places)
        return places
    '''######################################################################'''
    def numberOfShrink(self):
        '''
        Given the size of the board, decide the number of shrinking size
        '''
        if self.size ==8:
            return 0
        elif self.size == 6:
            return 1
        elif self.size == 4:
            return 2

    def shrinkBoard(self,shrink):
        '''
        Shrink the board given the number of shrinking.
        '''
        for row in range(0,8):
            for column in range(0,8):
                if (row < shrink or column < shrink or row > 7-shrink or
                    column > 7-shrink):
                    self.grid[column][row] = " "
        '''
        Shrink corners
        '''
        corners = [[shrink,shrink], [7-shrink, shrink], [7-shrink,7-shrink],
            [shrink,7-shrink]]

        for corner in corners:
            self.grid[corner[1]][corner[0]] = CORNER

    def eliminate(self,color):
        '''


        '''
        #Traverse all grid
        for column in range(len(self.grid)):
            for row in range(len(self.grid[column])):
                p = self.grid[column][row]
                #If the color is the opponent color and Possible to
                # Eliminate, remove it as empty.
                if p == getOpponent(color) and self.possibleEliminate((row,column)):
                    #print( " 消灭了"):
                    self.grid[column][row] = "-"

    def possibleEliminate(self,positions):
        '''
        Eliminating phase
        Need to consider pieces that are either on a same vertical axis
        or a horizontal axis
        '''
        column = positions[1]
        row = positions[0]
        piece = self.grid[column][row]
        opponent = getOpponent(piece)
        #Up and down, vertical axis
        try:
            up = self.grid[column][row-1]
            down = self.grid[column][row+1]
            if((up == opponent or up == CORNER) and (down == opponent or
                down == CORNER)):
                return True
        except:
            pass
        #Left and right, horizontal axis
        try :
            left = self.grid[column-1][row]
            right = self.grid[column+1][row]
            if((left == opponent or left == CORNER) and (right == opponent or
                right == CORNER)):
                return True
        except:
            pass
        return False

    def possibleMoves(self,color):
        '''
        Return a list of tuple containing position and possible moves.
        It is a 2-D tuple inside the list. Be careful when trying to get the return type.
        i.e [(current position),(possible position)]
        '''
        moves = []
        for column in range(len(self.grid)):
            for row in range(len(self.grid[column])):
                p = self.grid[column][row]
                if p == color:
                    for move in self.fourMoves((row,column)):
                        moves.append(((row,column),move))
        shuffle(moves)
        return moves

    def fourMoves(self,position):
        '''
        Check possible moves
        Return a list of possible moves
        '''
        column = position[1]
        row = position[0]
        moves = []
        #Up
        try :
            if(self.grid[column][row-1] == "-" and row-1 >=0):
                moves.append((row-1,column))
            elif(self.grid[column][row-2] == "-" and row-2>=0):
                moves.append((row-2,column))
        except:
            pass
        #Down.
        try :
            if(self.grid[column][row+1] == "-" and row+1<=7):
                moves.append((row+1,column))
            elif(self.grid[column][row+2] == "-" and row+2<=7):
                moves.append((row+2,column))
        except:
            pass
        #Left
        try :
            if(self.grid[column-1][row] == "-" and column-1>=0):
                moves.append((row,column-1))
            elif(self.grid[column-2][row] == "-" and column-2>=0):
                moves.append((row,column-2))
        except:
            pass
        #Right
        try :
            if(self.grid[column+1][row] == "-" and column+1 <=7):
                moves.append((row,column+1))
            elif(self.grid[column+2][row] == "-" and column+2<=7):
                moves.append((row,column+2))
        except:
            pass

        shuffle(moves)
        return moves

#####################################################################
#Functions out of Board obj
def boardInit():
    '''
    Initialise an empty board
    '''
    board = [['-' for x in range(0,8)] for y in range(0,8)]
    for index in [[0,0], [0,7], [7,7],[7,0]]:
        board[index[0]][index[1]] = CORNER
    return board

def getOpponent(color):
    '''
    Oponent color given the color of the player.
    '''
    if(color == WHITE):
        return BLACK
    else:
        return WHITE
