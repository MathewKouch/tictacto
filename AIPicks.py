def AIPicks(theBoard,turn,currentAIBestStrategy,currentPlayerBestStrategy,currentAIBest,currentPlayerBest):
    import random
    # Using a look up table to pick best position
    # Depends on location
    # Outputs
    AIPicksOutput=0 # THE SPOT ON THE BOARD
    boardAvailableSpaces = []        

    theBoardFS = theBoard.copy() # COPIES converts the board FILLED spots to 1, empty slots to 0

    for i in [1,2,3,4,5,6,7,8,9]:
        if theBoard[i] == 1: # AI spot taken
            theBoardFS[i] = 1
        elif theBoard[i] == -1: # Player spot
            theBoardFS[i] = -3
        elif theBoard[i] == 0: #Just empty spot
            theBoardFS[i] = 0

    for i in theBoard:
        if theBoard[i] == 0:
            boardAvailableSpaces.append(i)
    
    # Available strategies on board   
    tr_current_l = [[theBoardFS[1],1],[theBoardFS[2],2],[theBoardFS[3],3]]
    mr_current_l = [[theBoardFS[4],4],[theBoardFS[5],5],[theBoardFS[6],6]]
    br_current_l = [[theBoardFS[7],7],[theBoardFS[8],8],[theBoardFS[9],9]] 
        
    lc_current_l = [[theBoardFS[1],1],[theBoardFS[4],4],[theBoardFS[7],7]]
    mc_current_l = [[theBoardFS[2],2],[theBoardFS[5],5],[theBoardFS[8],8]] 
    rc_current_1 = [[theBoardFS[3],3],[theBoardFS[6],6],[theBoardFS[9],9]]
        
    bdiag_current_1 = [[theBoardFS[1],1],[theBoardFS[5],5],[theBoardFS[9],9]]
    fdiag_current_1 = [[theBoardFS[3],3], [theBoardFS[5],5],[theBoardFS[7],7]]

    currentStrategiesDic = {1:tr_current_l,2:mr_current_l,3:br_current_l,4:lc_current_l,5:mc_current_l,6:rc_current_1,7:bdiag_current_1,8:fdiag_current_1}
        
    chosenStrategyAI = currentStrategiesDic[currentAIBestStrategy] # [[theBoardFS[1],1],[theBoardFS[2],2],[theBoardFS[3],3]]
    playerSrategy = currentStrategiesDic[currentPlayerBestStrategy]
    
    if currentPlayerBest != -6: # JUST ATTACK aim for 3 in a row quick
        if ((chosenStrategyAI[0][0] or chosenStrategyAI[2][0]) == 1) and (chosenStrategyAI[1][0] == 0): # C: O/X space O/X  NEXT: O/X O O/X
            AIPicksOutput = chosenStrategyAI[1][1]
            print('Computer Chooses Stratgey With Edges. Picks Centre. Spot: ', AIPicksOutput)

            # Below 1 current O in middle
        elif (chosenStrategyAI[1][0] == 1) and (chosenStrategyAI[0][0] == 0): # Current: space O ? Next: O O ?
            AIPicksOutput = chosenStrategyAI[0][1]
            print('Computer Chooses Stratgey with Centre. Picks LEFT edge. Spot: ', AIPicksOutput)
        elif (chosenStrategyAI[1][0] == 1) and (chosenStrategyAI[1][0] == 0): # Current: ? O space NEXT: ? O O
            AIPicksOutput = chosenStrategyAI[2][1]
            print('Computer Chooses Stratgey with Centre. Pick RIGHT egde. Spot: ', AIPicksOutput)
            
            # Below has 2 current 0 in either side
        elif ((chosenStrategyAI[0][0] == 1) and (chosenStrategyAI[0][0] == 1)) and (chosenStrategyAI[2][0] == 0): # Current:  O O space Next: O O O
            AIPicksOutput = chosenStrategyAI[2][1]
            print('Computer Chooses Stratgey with Centre. Pick RIGHT egde. Spot: ', AIPicksOutput)
        elif ((chosenStrategyAI[1][0] == 1) and (chosenStrategyAI[2][0] == 1)) and (chosenStrategyAI[0][0] == 0): # Current: space O 0 Next: O O O
            AIPicksOutput = chosenStrategyAI[0][1]
            print('Computer Chooses Stratgey with Centre. Pick LEFT egde. Spot: ', AIPicksOutput)
        elif ((chosenStrategyAI[0][0] == 1) and (chosenStrategyAI[2][0] == 1)) and (chosenStrategyAI[1][0] == 0): # Current: space O 0 Next: O O O
            AIPicksOutput = chosenStrategyAI[1][1]
            print('Computer Chooses Stratgey with Centre. Pick MIDDLE. Spot: ', AIPicksOutput)
            
        else:
            AIPicksOutput = random.choice(boardAvailableSpaces) # strategy can't decide.
            print('Computer has NO IDEA, picks at RANDOM: Chooses spot: ', AIPicksOutput)
    elif (currentPlayerBest == -6) and (currentAIBest == 2):
        # Below has 2 current 0 in either side # PRIORITISE WINNING
        if ((chosenStrategyAI[0][0] == 1) and (chosenStrategyAI[0][0] == 1)) and (chosenStrategyAI[2][0] == 0): # Current:  O O space Next: O O O
            AIPicksOutput = chosenStrategyAI[2][1]
            print('Computer Chooses Stratgey with Centre. Pick RIGHT egde. Spot: ', AIPicksOutput)
        elif ((chosenStrategyAI[1][0] == 1) and (chosenStrategyAI[2][0] == 1)) and (chosenStrategyAI[0][0] == 0): # Current: space O 0 Next: O O O
            AIPicksOutput = chosenStrategyAI[0][1]
            print('Computer Chooses Stratgey with Centre. Pick LEFT egde. Spot: ', AIPicksOutput)
        elif ((chosenStrategyAI[0][0] == 1) and (chosenStrategyAI[2][0] == 1)) and (chosenStrategyAI[1][0] == 0): # Current: space O 0 Next: O O O
            AIPicksOutput = chosenStrategyAI[1][1]
            print('Computer Chooses Stratgey with Centre. Pick MIDDLE. Spot: ', AIPicksOutput)
            
        else:
            AIPicksOutput = random.choice(boardAvailableSpaces) # strategy can't decide.
            print('Computer has NO IDEA, picks at RANDOM: Chooses spot: ', AIPicksOutput)
    elif (currentPlayerBest == -6) and (currentAIBest != 2): # DEFENDINGGGGGG
        if ((playerSrategy[0][0] == -3) and (playerSrategy[0][0] == -3)) and (playerSrategy[2][0] == 0): # Current:  O O space Next: O O O
            AIPicksOutput = playerSrategy[2][1]
            print('Computer DEFENDS. Pick RIGHT egde. Spot: ', AIPicksOutput)
        elif ((playerSrategy[1][0] == -3) and (playerSrategy[2][0] == -3)) and (playerSrategy[0][0] == 0): # Current: space O 0 Next: O O O
            AIPicksOutput = playerSrategy[0][1]
            print('Computer DEFENDS. Pick LEFT egde. Spot: ', AIPicksOutput)
        elif ((playerSrategy[0][0] == -3) and (playerSrategy[2][0] == -3)) and (playerSrategy[1][0] == 0): # Current: space O 0 Next: O O O
            AIPicksOutput = playerSrategy[1][1]
            print('Computer Chooses Stratgey with Centre. Pick MIDDLE. Spot: ', AIPicksOutput)
        else:
            AIPicksOutput = random.choice(boardAvailableSpaces) # strategy can't decide.
            print('Computer has NO IDEA, picks at RANDOM: Chooses spot: ', AIPicksOutput)
        
            

    if AIPicksOutput != 0:
        theBoard[AIPicksOutput] = 1
    else:
        print('RANDOMMM shit')
  
    return AIPicksOutput 
    
        
    
        
    
