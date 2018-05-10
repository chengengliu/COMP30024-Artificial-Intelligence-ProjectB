def evaluate(self, board, step, playerColor, oppoColor):
        neighbors = [[1, 1], [1, 0], [0, 1], [-1, 0], [-1, -1], [0, -1], [-1, 1], [1, -1]]
        for neighbor in neighbors:
            i = 1 # whenever there is a opponent piece around player's piece, value-1
                  # but it will only be evaluated if there are more than oppo's piece
                  # hence the value point starts with 1
            if(len(step) == 1):
                #whenever a opponent piece, value - 1
                if (board[step[0] + neighbor[0]][step[1] + neighbor[1]] == oppoColor):
                    i -= 1
                #whenever a player piece around, value + 1
                elif (board[step[0] + neighbor[0]][step[1] + neighbor[1]] == playerColor):
                    i += 1
            else:
                if (board[step[1][0] + neighbor[0]][step[1][1] + neighbor[1]] == oppoColor):
                    i -= 1
                elif (board[step[1][0] + neighbor[0]][step[1][1] + neighbor[1]] == playerColor):
                    i += 1
        return i