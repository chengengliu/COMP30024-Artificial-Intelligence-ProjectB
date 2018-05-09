from Board import Board
from AlphaBeta import AlphaBeta

class Strategy:

    def possible_move(self, board, curr):
        d = len(board)
        return [(y, x) for y in range(d) for x in range(d) if board[y][x] == '']
    
    def next_state(self, oldBoard, player, oppo):
        import copy
        new = copy.deepcopy(oldBoard)
        new[oppo[0]][oppo[1]] = player
        return new

    def get_winner(self, board):
        if ('B' not in board ):
            return 'W'
        elif ('W' not in board):
            return 'B'
        elif (board.count('W') > board.count('B')):
            return 'W'
        elif (board.count('W') < board.count('B')):
            return 'B'
        else:
            return False
        

    def game_over(self, board):
        if (self.get_winner(board) is not None):
            return True
        elif (board.count('B') == board.count('W') == 2):
            return True

    def evaluate(self, board, playerColor):
        win = self.get_winner(board)
        if win is None:
            return 0
        return 10 if win == playerColor else -10
        