def readBoard(theBoard,turn):
    # Reads the board, looks at current winning strategies
    # Outputs the possible patterns for next placement of AI piece by:
    # 1) Seeing which pattern has avaialbel space
    # 2) Scoring each winning pattern
    currentScore = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0} # Scoring the 8 possible winning patterns
    BoardFilledSpots = currentScore.copy() # Counting the number of filled spot in each 8 winning patterns

    ####### STEP 1) Filled Spots
    
    theBoardFS = theBoard.copy() # COPIES converts the board FILLED spots to 1, empty slots to 0

    for i in [1,2,3,4,5,6,7,8,9]:
        if theBoard[i] == 1: # AI spot taken
            theBoardFS[i] = 1
        elif theBoard[i] == -1: # Player spot
            theBoardFS[i] = -3
        elif theBoard[i] == 0: #Just empty spot
            theBoardFS[i] = 0
        
        
        
    # Now counting number of filled spots in each of the 8 winning patterns
    # Checking if spot if full!
    
    tr_current_f = int(((theBoardFS[1]) + theBoardFS[2] + theBoardFS[3]))
    BoardFilledSpots[1] = tr_current_f
    
    mr_current_f = int((theBoardFS[4] + theBoardFS[5] + theBoardFS[6]))
    BoardFilledSpots[2] = mr_current_f
    
    br_current_f =  int((theBoardFS[7] + theBoardFS[8] + theBoardFS[9]))
    BoardFilledSpots[3] = br_current_f

    lc_current_f= int((theBoardFS[1] + theBoardFS[4] + theBoardFS[7])) 
    BoardFilledSpots[4] = lc_current_f

    mc_current_f = int((theBoardFS[2] + theBoardFS[5] + theBoardFS[8])) 
    BoardFilledSpots[5] = mc_current_f

    rc_current_f = int((theBoardFS[3] + theBoardFS[6] + theBoardFS[9]))
    BoardFilledSpots[6] = rc_current_f
        
    bdiag_current_f = int((theBoardFS[1] + theBoardFS[5] + theBoardFS[9])) 
    BoardFilledSpots[7] = bdiag_current_f

    fdiag_current_f = int(theBoardFS[3] + theBoardFS[5] + theBoardFS[7])
    BoardFilledSpots[8] = fdiag_current_f

    ####### STEP 2) Scoring Winning Patterns

    # Preallocating current score
    
    # Available strategies on board   
    #tr_current_l = [theBoard[1],theBoard[2],theBoard[3]]
    #mr_current_l = [theBoard[4],theBoard[5],theBoard[6]]
    #br_current_l [theBoard[7], theBoard[8], theBoard[9]] 
        
    #lc_current_l = [theBoard[1],theBoard[4],theBoard[7]]
    #mc_current_l = [theBoard[2],theBoard[5],theBoard[8]] 
    #rc_current_1 = [theBoard[3],theBoard[6],theBoard[9]]
        
    #bdiag_current_1 = [theBoard[1],theBoard[5],theBoard[9]]
    #fdiag_current_1 = [theBoard[3], theBoard[5],theBoard[7]]

    #currentStrategiesDic = {1:tr_current_l,2:mr_current_l,3:br_current_l,4:lc_current_l,5:mc_current_l,6:rc_current_1,7:bdiag_current_1,8:fdiag_current_1}
        
    # current scores   
    tr_current = (theBoard[1] + theBoard[2] + theBoard[3])
    mr_current = (theBoard[4] + theBoard[5] + theBoard[6]) 
    br_current = (theBoard[7] + theBoard[8] + theBoard[9]) 
        
    lc_current = (theBoard[1] + theBoard[4] + theBoard[7]) 
    mc_current = (theBoard[2] + theBoard[5] + theBoard[8]) 
    rc_current = (theBoard[3] + theBoard[6] + theBoard[9])
        
    bdiag_current = (theBoard[1] + theBoard[5] + theBoard[9]) 
    fdiag_current = (theBoard[3] + theBoard[5] + theBoard[7])

       
    # Storing score in LIST
    currentScore[1] = tr_current
    currentScore[2] = mr_current
    currentScore[3] = br_current

    currentScore[4] = lc_current
    currentScore[5] = mc_current
    currentScore[6] = rc_current

    currentScore[7] = bdiag_current
    currentScore[8] = fdiag_current

    currentScore = BoardFilledSpots
    #BoardFilledSpots = 



    #output = currentScoreList,BoardFilledSpots

    return currentScore,BoardFilledSpots # dictionary outputs
                                                           

    

    
        
