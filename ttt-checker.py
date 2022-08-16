#If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

#Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:

#[[0, 0, 1],
# [0, 1, 2],
# [2, 1, 0]]
#We want our function to return:

#-1 if the board is not yet finished AND no one has won yet (there are empty spots),
#1 if "X" won,
#2 if "O" won,
#0 if it's a cat's game (i.e. a draw).
#You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.

def is_solved(board):
    
    win = 0
    
    #check horizontal
    for row in board:
        if row[0] == row[1] and row[1] == row[2]:
            if row[0] == 1:
                return 1
            elif row[0] == 2:
                return 2
    
    #check vertical
    for column in range(len(board)):
        if board[0][column] == board[1][column] and board[1][column] == board[2][column]:
            if board[0][column] == 1:
                return 1
            elif board[0][column] == 2:
                return 2
            
    #check diagonal
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == 1:
            return 1
        elif board[0][0] == 2:
            return 2
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[2][0] == 1:
            return 1
        elif board[2][0] == 2:
            return 2
        
    #check cats/unfinished
    for row in board:
        for item in row:
            if item == 0:
                return -1
    return 0
