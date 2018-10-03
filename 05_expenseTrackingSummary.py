with open('testData/05_ExpenseTrackingData.txt') as f:
    INPUT = f.read().splitlines()

SUM_EXPENSE = 0
DAYS = len(INPUT)
for row in INPUT:
    PER_DAY_EXPENSE = row.split()
    if len(PER_DAY_EXPENSE) > 1:
        for i in range(len(PER_DAY_EXPENSE)-1):
            #print(PER_DAY_EXPENSE[i+1][1:])
            SUM_EXPENSE += float(PER_DAY_EXPENSE[i+1][1:])
#print(SUM_EXPENSE)
#print(DAYS)
print("{:.2f}".format(SUM_EXPENSE/DAYS))