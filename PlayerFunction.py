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

def legalPosition(row, column, shrink):
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
                        move+=1;
                    elif legalJump(board, row, column, shrink, dir):
                        move+=1;
    return number
