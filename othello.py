import random
ROW = 8
COLUMN = 8
PLAYER = 'B'
COMPUTER = 'W'

def vsAI():
    # the game against the computer
    black = 2
    white = 2
    board = buildBoard()
    print('BLACK:', black, '\tWHITE:',white)
    printBoard(board)
    play(board,black,white)
    return

'''
- - - - - - - - 
- - - - - - - - 
- - - - - - - - 
- - - W B - - - 
- - - B W - - - 
- - - - - - - - 
- - - - - - - - 
- - - - - - - - 
'''
def switchColor(c):
    # changes color to the opposite
    if c == PLAYER:
        return COMPUTER
    else:
        return PLAYER
        
def leftValidChoice(b,r,c,color):
    # check left
    if c > 1:
        c -= 1
        if b[r][c] == switchColor(color):
            while c > 1:
                c -= 1
                if b[r][c] == color:
                    return True
                elif b[r][c] == '-':
                    return False
    return False

def topLeftValidChoice(b,r,c,color):
    # check top left
    if c > 1 and r > 1:
        c-=1
        r-=1
        if b[r][c] == switchColor(color):
            while c > 1 and r > 1:
                c -= 1 
                r -= 1
                if b[r][c] == color:
                    return True
                elif b[r][c] == '-':
                    return False
    return False
  
def topRightValidChoice(b,r,c,color):
    # check top right
    if c > 1 and r < ROW - 1:
        c-=1
        r+=1
        if b[r][c] == switchColor(color):
            while c > 1 and r < ROW - 1:
                c -= 1 
                r += 1
                if b[r][c] == color:
                    return True
                elif b[r][c] == '-':
                    return False
    return False

def bottomLeftValidChoice(b,r,c,color):
    # check bottom left
    if c < COLUMN - 1 and r > 1:
        c+=1
        r-=1
        if b[r][c] == switchColor(color):
            while c < COLUMN - 1 and r > 1:
                c += 1
                r -= 1
                if b[r][c] == color:
                    return True
                elif b[r][c] == '-':
                    return False
    return False
    
def bottomRightValidChoice(b,r,c,color):
    # check bottom right
    if c < COLUMN - 1 and r < ROW - 1:
        c+=1
        r+=1
        if b[r][c] == switchColor(color):
            while c < COLUMN - 1 and r < ROW - 1:
                c += 1 
                r += 1
                if b[r][c] == color:
                    return True
                elif b[r][c] == '-':
                    return False
    return False
    
def rightValidChoice(b,r,c,color):                  
    # check right

    if c < COLUMN - 1:
        c += 1
        if b[r][c] == switchColor(color):
            while c < COLUMN - 1:
                c += 1
                if b[r][c] == color:
                    return True
                elif b[r][c] == '-':
                    return False
    return False
      
def topValidChoice(b,r,c,color):  
    # check top
    if r > 1:
        r -= 1
        if b[r][c] == switchColor(color):
            while r > 1:
                r -= 1
                if b[r][c] == color:
                    return True
                elif b[r][c] == '-':
                    return False
    return False
   
def bottomValidChoice(b,r,c,color):         
    # check bottom
    if r < ROW - 1:
        r += 1
        if b[r][c] == switchColor(color):
            while r < ROW - 1:
                r += 1
                if b[r][c] == color:
                    return True
                elif b[r][c] == '-':
                    return False
    return False

def boardNotFilled(b):
    # returns True if the board is not yet filled with both colors, otherwise return false
    for i in range(ROW):
        for j in range(COLUMN):
            if b[i][j] == '-':
                return True
    return False
    
def hintChoice(valid):
    # transforms the hint choices from the index form to actual real life row and column
    for i in range(len(valid)):
        valid[i][0] += 1
        valid[i][1] += 1
    return valid
    
def play(board,b,w):
    # start the game
    turn = PLAYER
    while boardNotFilled(board):
        if turn == PLAYER:
            validList = validPosition(board, turn)
            print('Hint: ',hintChoice(validList))
            print('Your turn:', PLAYER)
            while True:
                row = input('Enter row: ')
                col = input('Enter column: ')
                if row.isnumeric() and col.isnumeric():
                    row = int(row)
                    col = int(col)
                    if row >= 1 and col >= 1 and row <= ROW and col <= COLUMN:
                        if board[row-1][col-1] != '-':
                            print('Position Taken!')
                        elif leftValidChoice(board,row-1,col-1,turn) or \
                            rightValidChoice(board,row-1,col-1,turn) or \
                            topValidChoice(board,row-1,col-1,turn) or \
                            bottomValidChoice(board,row-1,col-1,turn) or \
                            topLeftValidChoice(board, row-1,col-1,turn)or\
                            topRightValidChoice(board, row-1,col-1,turn)or\
                            bottomLeftValidChoice(board, row-1,col-1,turn)or \
                            bottomRightValidChoice(board, row-1,col-1,turn):
                                board[row-1][col-1] = turn
                                break
                        else:
                            print('Invalid positions!')
                    else:
                        print('Row or column not in range[invalid]!')
                else:
                    print('Please enter row and column numbers!')
            
            updateBoard(board,row-1, col-1,turn)
            b, w = count(board)
            print('BLACK:', b, '\tWHITE:',w)
            printBoard(board)
            turn = switchColor(turn)
            print('Computer turn:', COMPUTER)
        
        else:
            validSpot = validPosition(board, turn)
            computerChoice = random.choice(validSpot)
            board[computerChoice[0]][computerChoice[1]] = turn
            updateBoard(board,computerChoice[0], computerChoice[1], turn)
            b, w = count(board)
            print('BLACK:', b, '\tWHITE:',w)
            printBoard(board)
            turn = switchColor(turn)
    
    gameResult(b,w)

def count(b):
    # returns the number of black and white pieces on the board
    black = 0
    white = 0
    for r in range(ROW):
        for c in range(COLUMN):
            if b[r][c] == 'B':
                black += 1
            elif b[r][c] == 'W':
                white += 1
    return [black, white]
    
def gameResult(b,w):
    # outputs the game condition and see who won
    if w > b:
        print('Congratulations! You Won!')
    elif w < b:
        print('Dang dang dangggggg, you lost!')
    else:
        print('IIIIIIIIITS A DRAAAWWWWWWW!')
    

def validPosition(b,t):
    # returns a list of valid positions of the given color
    validArr = []
    for i in range(ROW):
        for j in range(COLUMN):
            if leftValidChoice(b,i,j,t) or \
                rightValidChoice(b,i,j,t) or \
                topValidChoice(b,i,j,t) or \
                bottomValidChoice(b,i,j,t) or \
                topLeftValidChoice(b,i,j,t) or\
                bottomLeftValidChoice(b,i,j,t) or\
                topRightValidChoice(b,i,j,t) or\
                bottomRightValidChoice(b,i,j,t):
                    if b[i][j] == '-':
                        validArr.append([i,j])
    return validArr
    
            
def updateBoard(b,r,c,t):
    # update the board i.e flips the opposite color after the user or the AI makes the move
    row = r
    col = c
    if leftValidChoice(b,r,c,t):
        c -= 1
        while b[r][c] == switchColor(t):
            b[r][c] = t
            c -= 1
    
    c = col
    if rightValidChoice(b,r,c,t):
        c += 1
        while b[r][c] == switchColor(t):
            b[r][c] = t
            c+=1
    c = col
    if topValidChoice(b,r,c,t):
        r -= 1
        while b[r][c] == switchColor(t):
            b[r][c] = t
            r-=1
    r = row

    if bottomValidChoice(b,r,c,t):
        r += 1
        while b[r][c] == switchColor(t):
            b[r][c] = t
            r+=1
            
    r = row
    if topLeftValidChoice(b,r,c,t):
        r -= 1
        c -= 1
        while b[r][c] == switchColor(t):
            b[r][c] = t
            r-=1
            c-=1
    
    r = row
    c = col
    if topRightValidChoice(b,r,c,t):
        r += 1
        c -= 1
        while b[r][c] == switchColor(t):
            b[r][c] = t
            r+=1
            c-=1
    
    r = row
    c = col
    if bottomLeftValidChoice(b,r,c,t):
        r -= 1
        c += 1
        while b[r][c] == switchColor(t):
            b[r][c] = t
            r-=1
            c+=1 
    
    r = row
    c = col
    if bottomRightValidChoice(b,r,c,t):
        r += 1
        c += 1
        while b[r][c] == switchColor(t):
            b[r][c] = t
            r+=1
            c+=1
          
def buildBoard():
    # builds and returns the original board
    rowList = []
    for i in range(ROW):
        colList = []
        for j in range(COLUMN):
            if (i == 3 and j == 3) or (i == 4 and j == 4):
                colList.append('W')
            elif (i == 3 and j == 4) or (i == 4 and j == 3):
                colList.append('B')
            else:
                colList.append('-')
        rowList.append(colList)
    return rowList
    
'''
  1 2 3 4 5 6 7 8
1 - - - - - - - - 
2 - - - - - - - - 
3 - - - - - - - - 
4 - - - W B - - - 
5 - - - B W - - - 
6 - - - - - - - - 
7 - - - - - - - -
8 - - - - - - - -
'''
def printBoard(b):
    # displays the board 
    print('  ', end = '')
    for x in range(COLUMN):
        print(x + 1, end = ' ')
    print()
    for i in range(ROW):
        print(i+1, end = ' ')
        for j in range(COLUMN):
            print(b[i][j], end = ' ')
        print()

def rule():
    # game rule 
    print('''
    Black always moves first.
    If a player cannot outflank and flip at least one opposing disk, 
    they forfeit their turn and their opponent moves again. 
    However, if a move is available a player may not forfeit their turn.
    ''')

def menu():
    # the game menu
    while True:
        print('Welcome to Othello')
        print('1. Player vs Computer')
        print('2. Rule')
        print('3. Quit')
        option = input()
        if option == '1':
            vsAI() 
        elif option == '2':
            rule()
        elif option == '3':
            return 'Game Over!'
        else:
            continue

if __name__ == "__main__":
    # main function
    menu()















