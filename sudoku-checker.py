#checks to see if a sudoku board is completed or not

def done_or_not(board): #board[i][j]
    check = 0
    control = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    
    #horizontal check
    for i in board:
        mirror = set(i)
        if mirror != control:
            check += 1
        
    #vertical check
    for j in range(9):
        reverse = []
        for i in board:
            reverse.append(i[j])
        rmirror = set(reverse)
        if rmirror != control:
            check += 1
            
    #square check
    x = 3
    y = 3
    x2 = 0
    y2 = 0
    for t in range(3):
        for p in range(3):
            square = []
            for i in range(y2, y):
                for j in range(x2, x):
                    square.append(board[i][j])
                y += 1
                y2 += 1
            smirror = set(square)
            if smirror != control:
                check += 1
        y = 3
        y2 = 0
        x += 3
        x2 += 3

        
            
    if check == 0:
        return 'Finished!'
    else:
        return 'Try again!'
