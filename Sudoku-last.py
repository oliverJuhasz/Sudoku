"""
Sudoku game by Roland and Oliver. All rights reserved.
xyz
"""

import os
import platform
import random
import time
from colorama import init
from colorama import Fore, Back, Style


with open("title.txt","r") as f:
    cont =f.read()
    print (cont)

with open("sudoku-top95.txt", "r") as f:
    sudokus = f.readlines()

def import_sudoku(x):
    with open("sudoku-top95.txt", "r") as f:
        text = f.read()
        temp = text.split("\n")
        temp.pop(len(temp)-1)
        #print(temp)
        if x == "r":
            return fill_matrix(temp[random.randint(0,len(temp) - 1)])
        elif x > 0 and x < len(temp):
            return fill_matrix(temp[x - 1] )
        else:
            return fill_matrix(temp[1])

def fill_matrix(string):
    counter = 0
    MatrixList = [[0,1,8,0,0,0,0,3,0],[9,0,0,0,0,2,0,4,5],[7,0,0,0,0,6,0,0,0],[0,0,0,0,0,7,1,2,0],[0,0,0,0,5,0,0,0,0],[0,8,4,3,0,0,0,0,0],[0,0,0,7,0,0,0,0,6],[8,2,0,6,0,0,0,0,9],[0,3,0,0,0,0,5,8,0]]
    for y in range(0,9):
        for x in range(0,9):
            MatrixList[y][x] = int(string[counter])
            counter += 1
    return MatrixList

def print_matrix_values():
    pass

    
def print_sudoku2(board):  # A board a mátrix!!
    letters = tuple(("A","B","C","D","E","F","G","H","I"))
    print(f"{Fore.BLUE}            " + "  1 " + "  2 " + "  3 " + "  4 " + "  5 " + "  6 " + "  7 " + "  8 " + "  9 " + f"  {Style.RESET_ALL}")
    print("            " + "┏" + "━━━┳"*8 + "━━━┓")
    for i, row in enumerate(board):
        print((f"{Fore.BLUE}          " + str(letters[i] + f"{Style.RESET_ALL} " + "┃" + " {} │ {} │ {} ┃"*3).format(*[x if x != 0 else " " for x in row])))
        if i % 3 == 2:
            print("            " + "┣" + ("━━━┿"*2 + "━━━╋")*2 + "━━━┿"*2 + "━━━┫")
        elif i % 20 == 18:
            print("            " + "┗" + "━━━┻"*8 + "━━━┛")
        else:    
            print("            " + "┠" + ("───┼"*2 + "───╂")*2 + "───┼"*2 + "───┨")
    #print("            " + "┗" + "━━━┻"*8 + "━━━┛")

def newcord():
    try:
        x = input(" Enter a letter between A and I:  ").upper()
        ABC = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8}
        try:
            z = ABC[x]
        except KeyError:
            print("Wrong input ")
            x = input(" Enter a letter between A and I:  ")
            z = ABC[x] 
        valid_numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9,)
        y = (int(input(" Enter a number between 1-9 , ( 0 for clear your mistake ):  "))) - 1
        if y not in valid_numbers:
            print("Enter a valid number between 1-9 ")
            print(MatrixList2[z][y])
        else:
            print(MatrixList2[z][y])
        change = int(input(" Enter the new value:  "))
        if change not in valid_numbers:
            print("Enter a valid number between 1-9 ")
            change = int(input(" Enter the new value:  "))
        else:
            MatrixList2[z][y] = change
            update()
            if validation_checker():
                if check_verification():
                    return True
    except ValueError:
        print(f"{Fore.RED}Number between 1-9!{Style.RESET_ALL}")
                



def update():
    if platform.system() == 'Linux':
        os.system('clear')
        print(cont)
        print_sudoku2(MatrixList2)
    elif platform.system() == 'Windows':
        os.system('cls')
        print(cont)
        print_sudoku2(MatrixList2)      



def validation_checker():

    ValidationCheck = 0
    for i in range(0,9):
        if len(list(filter(filter_number,MatrixList2[i]))) == 9:
            ValidationCheck += 1

    templist = []
    for i in range(0,9):
        templist.clear()
        for i2 in range(0,9):
            templist.append(MatrixList2[i2][i])
        if len(list(filter(filter_number,templist))) == 9:
            ValidationCheck += 1

    if ValidationCheck == 18:
        return True
    else:
        return False

def filter_number(x):
    try:
        if 0 < x <10:
            return True
        else:
            return False
    except: return False

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

# A mátrix , a sudoku mezőinek értékeivel. Az értékek mátrix elemenként változtathatóak.

MatrixList2 = import_sudoku(1) #"r" for random sudoku
#for Line in range(0,9):
    #print(MatrixList[Line])


"""Itt következik maga a sudoku tábla."""

print_sudoku2(MatrixList2)

"""A koordinatak a 9x9-es táblát A1-től I9-ig osztják fel. Egy harmadik inputtal a kivalasztott mátrix pontra lehet
    új értéket megadni , illetve javítani az előző értéken."""

# Koordinatak és új értékek:

while True:
    try:
        if newcord() == True:
            break
    except KeyError:
        print(f"{Fore.RED}Please, write a single letter between A and I{Style.RESET_ALL}")

if platform.system() == 'Linux':
    os.system('clear')

elif platform.system() == 'Windows':
    os.system('cls')

    
print("Your winner!")

"""A győzelmi feltételek , illetve a helyes értékek ellenőrzése , eredmény megjelenítése"""

print("\n"*6)


if validation_checker() == True:
    print("Validation successful")
    if check_verification() == True:
        print("Solution accepted!")


    
        
