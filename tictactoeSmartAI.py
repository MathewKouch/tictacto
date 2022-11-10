def computerChoiceSMART(theBoard, turn): # "Intelligently" decides
    import random
    from readBoard import readBoard
    from tttBoardFunctions import computerChoice
    from AIPicks import AIPicks
    
    chosen = 0
    defend = 0
    attack = 0
    choiceStrategy = 'NO AI CHOICE MADE'

    [currentScore,BoardFilledSpots] = readBoard(theBoard,turn)
    
    if turn == 0: # AI goes first
        choice = 5
        theBoard[choice] = 1
    elif turn == 1: # else if AI goes second
        if (theBoard[5] == 0):
            choice = 5
            theBoard[choice] = 1
        else:
            attempt = 0
            cornersFull = 0
            while (chosen != 1 and (turn < 9))and(attempt <=5): # randomly picks a slot
                choice = random.choice([1,3,7,9])
                if (theBoard[choice] == 0): # if the choice slot is empty
                    theBoard[choice] = 1
                    chosen = 1
                attempt = attempt + 1
                if attempt >= 5:
                   cornersFull = 1
                   chosen = 0
            if cornersFull == 1:
                while chosen != 1 and (turn < 9): # randomly picks a slot
                    choice = random.randint(1,9)
                    chosen = (theBoard[choice] == 0) # if the choice slot is empty
                theBoard[choice] = 1

    if turn >= 2: #AI Second Move...Now we strategise
        print('Current Score List: ',currentScore)
        print('BoardFilledSpots: ',BoardFilledSpots)
        
        # Finding the maximimum scores
        # computerChoice(theBoard,turn)
        maxValue = -9999
        minValue = 9999
        index = 0
        for i in [1,2,3,4,5,6,7,8]:
            current_compare = int(currentScore[i])
            index = index + 1
            if current_compare > maxValue:  
                maxValue = current_compare
                maxindexValue = index
            if current_compare < minValue:
                minValue = current_compare
                minindexValue = index
                
        currentAIBest = maxValue
        currentAIBestStrategy = maxindexValue

        currentPlayerBest = minValue
        currentPlayerBestStrategy = minindexValue
        print('Best next move for AI is pattern no: ', currentAIBestStrategy)
        print('Best next move for PLAYER is pattern no: ',  currentPlayerBestStrategy)
        choiceStrategy = AIPicks(theBoard,turn,currentAIBestStrategy,currentPlayerBestStrategy,currentAIBest,currentPlayerBest)

        #Now we gotta choose wich slot in the strategy to pick from



        #if (currentAIBest >= currentPlayerBest) and (currentAIBest == 1):
         #   attack = 1 # attacking now, even if player is one move away from winning
          #  nextAIMove = currentStrategiesDic[currentAIBestStrategy]
            #if nextAIMove[0] == 1:
    
    return choiceStrategy
