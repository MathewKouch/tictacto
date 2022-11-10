import pprint
import random
import time
import string
from tictactoeSmartAI import computerChoiceSMART
from readBoard import readBoard

from tttBoardFunctions import winningCheck,computerChoice,theBoardPrinted


    
print('Welcome to my first shity game: Tic Tac Toe...toes?')
print(' 1 | 2 | 3 ')
print('----------')
print(' 4 | 5 | 6 ')
print('----------')
print(' 7 | 8 | 9 ')

print('Above is the board. You are X.')
play = 'Y'
while play == 'Y':
    play = (input('Do you want to play? Y/N '))
    theBoard = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0} # todo first to do



    while play.upper() == 'Y':
        print('Game on bitch! Lets play!')

        winner = 0 # No winners at start of game
        turn = 0 # counts the number of turns of Player
        theBoardPrinted(theBoard)
        while winner != 1:
            
            if (turn == 9) and (winner == 0):
                winner = 1 # force the game to quit
                print('It is a draw!')
                
            playerChoice = int(input('Place X in position: '))
            while theBoard[playerChoice] != 0: # 0 means EMPTY. So not empty means PICK AGAIN
                playerChoice = int(input('Not Empty, try again. Place X in position '))  
            theBoard[playerChoice] = -1
            turn = turn + 1
            print('Turn: ', turn)
            theBoardPrinted(theBoard)
            
            

            winner = winningCheck(theBoard,'YOU',turn)
            time.sleep(0.1)
            
            if winner != 1: # Computers turn


                print('Computer Turn')
                AIchoice = computerChoiceSMART(theBoard,turn)
                print('Computer Chooses Strategy ', AIchoice)
                turn = turn + 1
                print('DONE! Turn: ', turn)

                theBoardPrinted(theBoard)
                winner = winningCheck(theBoard,'COMPUTER',turn)
            

        play = (input('Would you like to play again? Y/N '))
        theBoard = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}


    print('Goodbye! :)')
    break

            
        
    
