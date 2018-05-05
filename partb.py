import copy
import time
import PriorityQueue

class Board():

    def __init__(self):
        self.board = None
        self.characters = ['-', 'X', 'O', '@']
    def format():

    def analyseBoard():

    '''Return the char of a given position.
    '''
    def getChar(self, position):
        ifposition[0] > 7 or position[1] > 7 or position[0] < 0 or position[1] < 0:
            return '';
        positionX = position[0]
        positionY = position[1]
        char = self.board[positionX][positionY]
        return char
    ''' Return a list that contains the coordinates of the given chars.
    '''
    def getPositionOfChar(sefl, char, boardSize):
        charList = [];
        if char not in self.characters:
            return None;
        for i in range(0,boardSize):
            for j in range(0,boardSize):
                if char== self.board[i][j]:
                    charList.append((i,j));
        return charList;
