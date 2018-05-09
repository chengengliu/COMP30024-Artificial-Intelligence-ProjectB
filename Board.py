# Board are used to save the game board
# Board will update its chess pieces' location on every step

class Board:

    board = [['X','','','','','','','X'],
             ['','','','','','','',''],
             ['','','','','','','',''],
             ['','','','','','','',''],
             ['','','','','','','',''],
             ['','','','','','','',''],
             ['','','','','','','',''],
             ['X','','','','','','','X']]


    def updateBoard(self, step, color):
        self.color = color
        self.step = step
        
        if(len(self.step) == 1):
            Board.board[self.step[0]][self.step[1]] = self.color[0]
        else:
            Board.board[self.step[0][0]][self.step[0][1]] = ''
            Board.board[self.step[1][1]][self.step[1][1]] = self.color[0]
