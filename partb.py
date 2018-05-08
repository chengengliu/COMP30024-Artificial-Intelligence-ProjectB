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


class Piece ():
	#position contains the coordinates of the piece. (as a list)

	def __init__(self, position, parent, startPoint=0, goalPosition = 0):
		self.children = []
		self.parent = parent
		self.position = position
		self.cost = 0
		if parent:
			self.path = [position]
			self.startPoint = startPoint
			self.goalPosition = goalPosition
		else:
			self.path = parent.path[:]
			self.startPoint = parent.startPoint
			self.goalPosition = parent.goalPosition
			self.path.append(self.position)

class ConcretePiece(Piece):

	def __int__(self,position, parent,surrounding, startPoint = 0, goalPosition = 0):
		#invoke a super constructor
		super(ConcretePiece,self).__int__(position,parent,startPoint,goalPosition)
		self.surrounding = deepcopy(surrounding)
		self.distance = self.calculateDistance()


	def children(self):
		#下上右左
		direction = [(0,1), (0,-1), (1,0), (-1,0)]

		#If current piece is not child
		if not self.children:
			for i in range(0,4):
				# First case, when there is no surrounding pieces around
				#i.e. it can move freely (no jumping here)
				#上下左右 都要看
				newColumn = self.position[0] + direction[i][0]
				newRow = self.position[1] + direction[i][1]
				#If out of bounds, skip the move
				if(newColumn > 7 or newColumn < 0
					or newRow > 7 or newRow < 0):
					continue
				if(self.surrounding[newRow][newColumn] == 'X'):
					continue

				#New position
				newPosition = (newColumn, newRow)

				#if the new position is empty(ie.free to move )
				if(self.surrounding[newRow][newColumn] == '-'):
					newSurrounding = deepcopy(self.surrounding)
					#The piece has moved so the original position become unocupied.
					#Move to the new position and posess the position as 'O'
					# I have to switch 0 and 1 order because the oder of the board
					# is the reverse of the coordinates
					newSurrounding[self.position[1]][self.position[0]] = '-'
					newSurrounding[newPosition[1]][newPosition[0]] = 'O'
					#Make the child node
					#Add it to child list
					child = ConcretePiece(position, self, newSurrounding)
					self.children.append(child)
					continue
				#Reinitialise the position movement
				# Now considering jumping
				newNewColumn = self.position[0] + direction[i][0]
				newNewRow = self.position[1] + direction[i][1]
				newNewPosition = (newNewColumn,newNewRow)
				# If the next of the next move is free and the next move is
				# possessed by other pieces(no matter what color is )
				if((self.surrounding[newNewRow][newNewColumn] == '-') and
					(surrounding[newRow][newColumn] == 'O' or '@')):
					#Similarly as above, change the original position to '- free'
					# Change the next new postion to 'O 'possessed
					newSurrounding = deepcopy(self.surrounding)
					newSurrounding[self.position[0]][self.position[1]] = '-'
					newSurroundingp[newNewPosition[0]][newNewPosition[1]] = 'O'
					child = ConcretePiece(position, self, newSurrounding)
					self.children.append(child)
				#If the next position is out of bounds or hit a conner
				#Skip move
				if((self.surrounding[newRow][newColumn] == 'O' or '@' or'X') and
					(newNewRow> 7 or newNewRow < 0 or newNewColumn > 7 or newNewColumn < 0)):
					continue
				if((self.surrounding[newRow][newColumn] == 'O' or '@' or 'X') and
					(self.surrounding[newNewRow][newNewColumn] == 'O' or '@')):
					continue

	#This should be the priority rule(or should we call it the heuristic function ? LOL )
	def calculateDistance(self):
		distance = abs(self.position[0] - self.goalPosition[0]) + abs(self.postion[1]-self.goalPosition[1])
		#Reach the goalPosition
		if(self.position[0] == self.goalPosition[0] and self.position[1] == self.goalPosition[1]):
			return 0
		return distance



class MinMax():
    def __init__(self, game):
        self.game = game
        self.currentNode = None
        self.successors = []

    def minMax(node):
        nodeList = []
        while not terminal(node):


    def terminal(self, node):
        return len(node.children) == 0
    def bestValue(node):
        if terminal(noe):
            return node.value
        maxValue = 0
        successors = node.children
        for child in successors:
            oldMax = maxValue
            maxValue = max(maxValue, child.value)
