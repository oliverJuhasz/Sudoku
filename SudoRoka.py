import os
import platform
import random
import time

def check_validation():
    ValidationCheck = 0  
    for i in range(0,9):
        if len(list(filter(lambda x: 10 > x > 0,MatrixList2[i]))) == 9:
            ValidationCheck += 1
        templist = [[i2][0] for i2 in range(0,9)]
        if len(list(filter(lambda x: 10 > x > 0,templist))):
            ValidationCheck += 1
    return True if ValidationCheck == 18 else False

def check_verification():
    check_verification = 0
    for i in range(0,9):
        if len(set(MatrixList2[i])) == len(MatrixList2[i]):
            check_verification += 1

    templist = []
    for i in range(0,9):
        templist.clear()
        for i2 in range(0,9):
            templist.append(MatrixList2[i2][i])
        if len(set(templist)) == len(templist):
            check_verification += 1

    for block in range(0,7,3):
        for block2 in range(0,7,3):
            templist.clear()
            for i in range(0,3):
                for i2 in range(0,3):
                    templist.append(MatrixList2[i2 + block][i + block2])
            if len(set(templist)) == len(templist):
                check_verification += 1
    if check_verification == 27:
        return True
    else:
        return False


MatrixList = [\
[1,8,4,9,6,3,7,2,5],
[5,6,2,7,4,8,3,1,9],
[3,9,7,5,1,2,8,6,4],
[2,3,9,6,5,7,1,4,8],
[7,5,6,1,8,4,2,9,3],
[4,1,8,2,3,9,6,5,7],
[9,4,1,3,7,6,5,8,2],
[6,2,3,8,9,5,4,7,1],
[8,7,5,4,2,1,9,3,6]]

MatrixList2 = MatrixList

print(check_validation())
print(check_verification())

#list(sorted(inventory.items(), key=lambda x: x[1],reverse=False))