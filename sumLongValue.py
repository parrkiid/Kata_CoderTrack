TOOD = "0"
def sumLongValue(INPUT1, INPUT2):
    OUTPUT = ""
    global TOOD
    TOOD = "0"
    for Index in reversed(range(len(INPUT1))):
        Sum = str(int(INPUT1[Index]) + int(INPUT2[Index])+ int(TOOD))
        Sum = TOOD_when_Sum_MoreThan_9(Sum)
        OUTPUT = Sum + OUTPUT
        
    return OUTPUT

def TOOD_when_Sum_MoreThan_9(Sum):
    global TOOD
    if int(Sum) > 9:
        TOOD = Sum[0]
        return Sum[1]
    else:
        TOOD = 0
        return Sum[0]