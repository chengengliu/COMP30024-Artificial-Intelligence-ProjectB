#PlayerFunction,py
'''
This .py file supplementary for other classes or functions.

'''

def boardInit():
    '''
    Initialise an empty board
    '''
    board = [['-' for x in range(0,8)] for y in range(0,8)]
    print(board)
    for index in [[0,0], [0,7], [7,7],[7,0]]:
        board[index[0]][index[1]] = 'X'

    return board
#boardInit()
#print(boardInit())
def printBoard(board):
    '''
    Print the current board in a nicer format.
    '''
    for row in range(0,8):
        temp = ""
        for column in range(0,8):
            temp = temp + board[column][row] + " "
        print(temp)
#printBoard(boardInit())

def getChar(board, row, column):
    '''
    Get the char at given position
    '''
    if position[0] > 7 or position[1] > 7 or position[0] < 0 or position[1] < 0:
        return '';
    char = board[column][row]
    return char

def legalPosition(column, row, shrink=None):
    '''
    Check if the position is still legal.
    May be used later in the shrinking phase.
    param shrink: indicate the number of times of shrinking roundself.
    i.e, if the first time shrinking, 8*8->6*6, shrink = 1 etc.
    '''
    size = 0
    if(shrink == None):
        pass
    else:
        size = shrink
    if (row not in range(size, 8-size)):
        return False
    if (column not in range(size,8 - size)):
        return False
    return True
def shrinkSize(rounds):
    '''
    Return the number of shrinking size.
    '''
    if(rounds < 128):
        return 0
    if(rounds >= 192):
        return 2
    if(rounds <192 and rounds >=128):
        return 1

def numberOnBoard(board):
    '''
    Return the number available on the board
    '''
    number = 0
    for column in range(0,8):
        for row in range(0,8):
            if board[column][row] == 'O' or board[column][row] == '@':
                number+=1
    return number

def makeMoveJump(board, row, column, shrink, dir):
    '''
    Do move. Check if it is legal before setting the new location
    Will use legalMove, legalJump, move, jump. Four functions
    '''
    if(legalMove(board, row, column, shrink, dir)):
        return move(board, row, column, shrink, dir);
    elif(legalJump(board, row, column, shrink, dir)):
        return jump(board, row, column, shrink, dir);
    return None

def move(board, row, column, shrink, dir):
    '''
    移动棋子。()无需再做检查，在call之前已经做过检查了。)

    return a List of new Location
    '''
    currentLocation = [column, row];
    #Up Down Left Right
    if(dir == 'up'):
        board[column][row-1] = board[column][row]
        board[column][row] = '-'
        newLocation = [column, row-1]
    elif(dir == 'down'):
        board[column][row+1] = board[column][row]
        board[column][row] = '-'
        newLocation = [column, row-1]
    elif(dir == 'left'):
        boad[column-1][row] = board[column][row]
        board[column][row] = '-'
        newLocation = [column-1, row]
    elif(dir == 'right'):
        board[column+1][row] = board[column][row]
        board[colu][row] = '-'
        newLocation = [column+1,row]
    return newLocation

def jump(baord, row, column, shrink, dir):
    '''
    棋子跳跃。（无需再做检查，在call之前已经做过检查了）
    return a List of New Location
    '''
    currentLocation = [column, row]
    if(dir == 'up'):
        board[column][row-2] = board[column][row]
        board[column][row] = '-'
        newLocation = [column, row-2]
    elif(dir == 'down'):
        board[column][row+2] = board[column][row]
        board[column][row] = '-'
        newLocation = [column, row-2]
    elif(dir == 'left'):
        boad[column-2][row] = board[column][row]
        board[column][row] = '-'
        newLocation = [column-2, row]
    elif(dir == 'right'):
        board[column+2][row] = board[column][row]
        board[colu][row] = '-'
        newLocation = [column+2,row]
    return newLocation

def legalMove(board, row, column, shrink, dir):
    '''
    查看下一步moving direction是否合法。 不包括跳跃
    Return boolean
    whether a move is legal or not. (excluding jump)
    '''
    if(dir == 'up'):
        if(legalPosition(row-1, column,shrink) and
            board[column][row-1] == '-'):
            return True
    if(dir == 'down'):
        if(legalPosition(row+1,column,shrink) and
            board[column][row+1] == '-'):
            return True
    if(dir == 'left'):
        if(legalPosition(row,column-1, shrink) and
            board[column-1][row] == '-'):
            return True
    if(dir == 'right'):
        if(legalPosition(row, column+1,shrink) and
            board[column+1][row] == '-'):
            return True
    return False

def legalJump(board, row, column, shrink, dir):
    '''
    查看下一步跳跃方向是否合法。
    这个function默认call的时候已经知道无法move或者说首选并非normal move
    '''
    if(dir == 'up'):
        if(legalPosition(row-2, column,shrink) and
            board[column][row-2] == '-'):
            return True
    if(dir == 'down'):
        if(legalPosition(row+1,column,shrink) and
            board[column][row+2] == '-'):
            return True
    if(dir == 'left'):
        if(legalPosition(row,column-2, shrink) and
            board[column-2][row] == '-'):
            return True
    if(dir == 'right'):
        if(legalPosition(row, column+2,shrink) and
            board[column+2][row] == '-'):
            return True
    return False

def tryMoves(board, piece, shrink):
    '''
    Return number of legal moves.
    Piece是需要检查的的Piece type. i.e, 'O' or '@'
    '''
    number = 0
    directions = ['up', 'down', 'left', 'right'];
    for row in range(0,8):
        for column in range(0,8):
            if(board[column][row] == piece):
                for dir in directions:
                    if legalMove(board,row, column, shrink,dir):
                        number+=1;
                    elif legalJump(board, row, column, shrink, dir):
                        number+=1;
    return number


def hasNeighbour(board, row, column):
    '''
    查看当前棋子是否被包围了
    检查当前棋子的邻居
    '''
    check = getChar(board, row, column)
    if(check not in ['O','@']):
        return None
    if(check == '@'):
        neighbour = ['O','X'];
    else:
        neighbour = ['@','X'];
    directions = [[[-1,0], [1,0]], [[0,-1], [0,1]]]

    for dir in directions:

        #e = [c[0][1], c[0][0]]
    	#f = [c[1][1], c[1][0]]
        #Need test later. Hardcoded test pass
        firstNeighbour = [dir[0][1]+row,dir[0][0]+column] # first Half(0,-1)(-1,0) up left
        secondNeighbour =[dir[1][1]+row,dir[1][0]+column] # second Half(0,1)(1,0) down right
        if(legalPosition(firstNeighbour[1],firstNeighbour[0]) and
            legalPosition(secondNeighbour[1],secondNeighbour[0])):
            #If the neighouburs are legal positions
            if(board[secondNeighbour[1]][secondNeighbour[0]] in neighbour and
                board[firstNeighbour[1]][firstNeighbour[0]] in neighbour):
                #If there is enemy(X or enemy) in the enighbours
                return True
    return False

def boardShrink(board, shrink):
    '''
    Shrink the board
    shrink: The number of shrink times
    return a shrinked board

    '''
    for row in range(0,8):
        for column in range(0,8):
            if row < shrink or column < shrink or row > 7-shrink or column > 7-shrink:
                board[column][row] = " "

    '''
    Remember to update the corner as well
    '''
    corners = [[shrink,shrink], [7-shrink, shrink], [7-shrink,7-shrink],
        [shrink,7-shrink]]
    for corner in corners:
        board[corner[1]][corner[0]] = 'X'
    return board


def updateBoard(board, player, playerP, opponentP):
    '''

#目前还没想好，因为我需要一个action，但是对于action的定义还不是很清晰
    Update the board according to the player board
    Return an updated board.
    '''
    return board
