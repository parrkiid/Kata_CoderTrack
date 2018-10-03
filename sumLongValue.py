def sumLongValue(INPUT1, INPUT2):
    OUTPUT = ""
    CARRY_NUMBER = "0"
    for Index in reversed(range(len(INPUT1))):
        Sum = str(int(INPUT1[Index]) + int(INPUT2[Index])+ int(CARRY_NUMBER))
        CARRY_NUMBER = CARRY_NUMBER_when_Sum_MoreThan_9(Sum)
        Sum_OUTPUT = OUTPUT_when_Sum_MoreThan_9(Sum)
        OUTPUT = Sum_OUTPUT + OUTPUT
        
    return OUTPUT

def CARRY_NUMBER_when_Sum_MoreThan_9(Sum):
    if int(Sum) > 9:
        return Sum[0]
    return "0"

def OUTPUT_when_Sum_MoreThan_9(Sum):
    if int(Sum) > 9:
        return Sum[1]
    return str(Sum)