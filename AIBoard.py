WHITE = "O"
BLACK = "@"
CORNER = "X"
EMPTY = "-"
class Board:
    def __init__(self,color):
        if color == 'white':
            color = WHITE
        else:
            color = BLACK
        self.player = color
        self.playerPieces = 0
        self.opponentPieces = 0
        self.size = 8
        self.grid = boardInit()
        self.opponent = opponent(color)
        self.shrinkBoard(numberOfShrink())

    def numberOfShrink():
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
            self.gird[corner[1]][corner[0]] = CORNER

    def makeMove(self, color, origin, goal):
        '''
        Make move from an original point to a goal point.
        It is called after it being checked as it is proper to move.
        '''
        columnFrom = origin[1]
        rowFrom = origin[o]
        columnTo = goal[1]
        rowTo = goal[0]
        self.grid[columnFrom][rowFrom] = "-"
        self.gird[columnTo][rowTo] = color
        self.update(color)


    def update(self,color):
        pass



    def eliminate(self,color):
        #Traverse all grid
        for column in range(len(self.grid)):
            for row in range(len(self.grid[column])):
                p = self.grid[column][row]
                #If the color is the opponent color
                if p == opponent(color) and self.possibleEliminate((row,column)):
                    self.grid[column][row] = "-"
        return None

    def possibleEliminate(self,positions):
        column = positions[1]
        row = positions[0]
        piece = self.grid[column][row]
        opponent = opponent(piece)
        '''
        Eliminating phase
        Need to consider pieces that are either on a same vertical axis
        or a horizontal axis
        '''
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
            if((left == opopnent or left == CORNER) and (right == opponent or
                right == CORNER)):
                return True
        except:
            pass
        return False

    def possiblePlacing(color):
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
        return places

    def possibleMoves(color):
        '''
        Return a list of tuple containing position and possible moves.

        '''
        moves = []
        for column in range(len(self.grid)):
            for row in range(len(self.grid[column])):
                p = self.grid[column][row]
                if p == color:
                    for move in self.fourMoves((row,column)):
                        moves.append(((row,column),move))
        return moves

    def fourMoves(position):
        '''
        Check possible moves
        Return a list of possible moves
        查看上下左右 Try
        ######################这里有个问题，这个list做出来，move的方向是根据谁来决定的。 
        '''
        column = position[1]
        row = position[0]
        moves = []
        #Up
        try :
            if(self.gird[column][row-1] == "-" and row-1 >=0):
                moves.append((row-1,column))
            elif(self.grid[column][row-2] == "-" and row-2>=0):
                moves.append((row-1,column))
        except:
            pass
        #Down
        try :
            if(self.gird[column][row+1] == "-" and row+1<=7):
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
                moves.appent((row,column+1))
            elif(self.grid[column+2][row] == "-" and column+2<=7):
                moves.append((row,column+2))
        except:
            pass
        return moves

#####################################################################
#Functions out of Board obj
def boardInit():
    '''
    Initialise an empty board
    '''
    board = [['-' for x in range(0,8)] for y in range(0,8)]
    #print(board)
    for index in [[0,0], [0,7], [7,7],[7,0]]:
        board[index[0]][index[1]] = CORNER
    return board

def opponent(color):
    '''
    Oponent color given the color of the player.
    '''
    if(color == WHITE):
        return BLACK
    else:
        return WHITE

def empty_grid(size):
    '''
    A total empty board with all "-"
    '''
    grid = [[EMPTY for i in range(size)] for i in range(size)]
    return grid
'''
grid = empty_grid(8)
print(len(grid[1]))
for column in range(len(grid)):
    for row in range(len(grid[column])):
        print (column,row)
#print (grid)
grid2 = boardInit()
#print(grid2)
print(len(grid))
'''
