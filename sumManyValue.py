def sumManyValue(DATA):
    INPUT1 = ""
    INPUT2 = ""
    OUTPUT = ""
    CURRENT_SUM = DATA[0]
    for INDEX in range(len(DATA)-1):
        INPUT1 = str(CURRENT_SUM)
        INPUT2 = str(DATA[INDEX+1])

        INPUT2 = setLengthOfINPUT2_to_Equal_to_INPUT1(INPUT1,INPUT2)
        INPUT1 = setLengthOfINPUT1_to_Equal_to_INPUT2(INPUT1,INPUT2)
        
        #print(INPUT1, INPUT2)
        OUTPUT = ""
        CARRY_NUMBER = "0"
        for Index in reversed(range(len(INPUT1))):
            Sum = str(int(INPUT1[Index]) + int(INPUT2[Index])+ int(CARRY_NUMBER))
            if isFirstPosition(Index):
                CARRY_NUMBER = CARRY_NUMBER_when_Sum_MoreThan_9(Sum)
                Sum = OUTPUT_when_Sum_MoreThan_9(Sum)
            OUTPUT = Sum + OUTPUT
        CURRENT_SUM = OUTPUT
        
    return(OUTPUT)

def isFirstPosition(Index):
    if Index != 0:
        return True
    return False

def setLengthOfINPUT1_to_Equal_to_INPUT2(INPUT1,INPUT2):
    if len(INPUT2)>len(INPUT1):
        DIFF_LENGTH = len(INPUT2)-len(INPUT1)
        MORE_LENGTH = ""
        for INDEX in range(DIFF_LENGTH):
            MORE_LENGTH += "0"

        RETURN_RESULT = MORE_LENGTH + INPUT1
        return RETURN_RESULT
    return INPUT1

def setLengthOfINPUT2_to_Equal_to_INPUT1(INPUT1,INPUT2):
    if len(INPUT1)>len(INPUT2):
        DIFF_LENGTH = len(INPUT1)-len(INPUT2)
        MORE_LENGTH = ""
        for INDEX in range(DIFF_LENGTH):
            MORE_LENGTH += "0"

        RETURN_RESULT = MORE_LENGTH + INPUT2
        return RETURN_RESULT
    return INPUT2

def CARRY_NUMBER_when_Sum_MoreThan_9(Sum):
    if int(Sum) > 9:
        return Sum[0]
    return "0"

def OUTPUT_when_Sum_MoreThan_9(Sum):
    if int(Sum) > 9:
        return Sum[1]
    return str(Sum)