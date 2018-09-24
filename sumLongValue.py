INPUT1 = "341958380513922689345579269516458072674896"
INPUT2 = "452266679609279263090069747948272865233879"
TOOD = "0"
OUTPUT = ""
print(len(INPUT1))
for Index in reversed(range(42)):
    Sum = str(int(INPUT1[Index]) + int(INPUT2[Index])+ int(TOOD))
    if Index != 0:
        TOOD = "0"
        if len(Sum) == 2:
            TOOD = Sum[0]
            Sum = Sum[1]
        else:
            TOOD = 0
    
    OUTPUT = Sum + OUTPUT
    
print(OUTPUT)


