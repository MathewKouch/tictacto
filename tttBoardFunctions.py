import random

def winningCheck(theBoard,player,turn):
    gameOver = 0 # default state is no winners detected. Game not over yet.
    if turn >=5:
        if (theBoard[1] == theBoard[2] == theBoard[3]) and (theBoard[2] != 0): # top row
            gameOver = 1
            case = 1
            print(case)
        elif (theBoard[4] == theBoard[5] ==theBoard[6]) and (theBoard[5]!= 0): # middle row
            gameOver = 1
            case = 2
            print(case)

        elif (theBoard[7] == theBoard[8] == theBoard[9]) and (theBoard[8] != 0): # bot row
            gameOver = 1
            case = 3
            print(case)
        
        elif (theBoard[1] == theBoard[4] == theBoard[7]) and (theBoard[4] != 0 ):# left column
            gameOver = 1
            case = 4
            print(case)
      
        elif (theBoard[2] == theBoard[5] == theBoard[8]) and (theBoard[5] != 0 ): # middle column
            gameOver = 1
            case = 5
            print(case)

        elif (theBoard[3] == theBoard[6] == theBoard[9]) and (theBoard[6] !=0): # right column
            gameOver = 1
            case = 6
            print(case)

        elif (theBoard[1] == theBoard[5] == theBoard[9]) and (theBoard[5] !=0): # backslash diagonal
            gameOver = 1
            case = 7
            print(case)
     
        elif (theBoard[3] == theBoard[5] == theBoard[7]) and (theBoard[5] !=0): # forwad slash diagonal
            gameOver = 1
            case = 8
            print(case)

        if gameOver == 1:
            print('Congratulations ', player, ' is the WINNER!')
            
        if (gameOver !=1) and (turn == 9):
            gameOver = 1
            print('It is a DRAW. No winners!')

    return gameOver

def computerChoice(theBoard,turn):
    chosen = ''
    while chosen != 1 and (turn < 9): # randomly picks a slot
        choice = random.randint(1,9)
        chosen = (theBoard[choice] == 0) # if the choice slot is empty

    if chosen == 1:
        theBoard[choice] = 1
        
        
def theBoardPrinted(theBoard):
    theBoardPs = list(range(1,13)) # dictionary translation of the Board to strings

    for i in [1,2,3,4,5,6,7,8,9]:
        if theBoard[i] == 1: # AI input dispay NAUGHT O
            theBoardPs[i] = 'O'
        elif theBoard[i] == -1: # Player input display CROSS X
            theBoardPs[i] = 'X'
        elif theBoard[i] == 0:
            theBoardPs[i] = ' '


          
    #print(' ',theBoard[1],' | ', theBoard[2], ' | ', theBoard[3], ' ')
    #print('-------------')
    #print(' ',theBoard[4],' | ', theBoard[5], ' | ', theBoard[6], ' ')
    #print('-------------')
    #print(' ',theBoard[7],' | ', theBoard[8], ' | ', theBoard[9], ' ')



    #for i in [1,2,3,4,5,6,7,8,9]:  
    print(' ',theBoardPs[1],' | ', theBoardPs[2], ' | ', theBoardPs[3], ' ')
    print('-------------')
    print(' ',theBoardPs[4],' | ', theBoardPs[5], ' | ', theBoardPs[6], ' ')
    print('-------------')
    print(' ',theBoardPs[7],' | ', theBoardPs[8], ' | ', theBoardPs[9],' ')
