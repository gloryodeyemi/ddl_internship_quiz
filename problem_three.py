#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    money_spent = []
    money_return = 0
    # Write your code here.
    for x in keyboards:
        for y in drives:
            money_spent.append(x+y)
            
    money_spent.sort(reverse=True)
    
    for money in money_spent:
        if money <= b:
            money_return += money
            break
        else:
            continue
    
    if money_return > 0:
        return money_return
    else:
        return -1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
