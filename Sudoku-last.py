"""
Sudoku game by Roland and Oliver. All rights reserved.

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

def ValueCheck(x,y):
    return True if matrix_list_original[x][y] > 0 else False

def SudokuImport(x):
    with open("sudoku-top95.txt", "r") as f:
        text = f.read()
        temp = text.split("\n")
        temp.pop(len(temp)-1)
        #print(temp)
        if x == "r":
            return MatrixFill(temp[random.randint(0,len(temp) - 1)])
        elif x > 0 and x < len(temp):
            return MatrixFill(temp[x - 1] )
        else:
            return MatrixFill(temp[1])

def MatrixFill(string):
    counter = 0
    MatrixList = [[0,1,8,0,0,0,0,3,0],[9,0,0,0,0,2,0,4,5],[7,0,0,0,0,6,0,0,0],[0,0,0,0,0,7,1,2,0],[0,0,0,0,5,0,0,0,0],[0,8,4,3,0,0,0,0,0],[0,0,0,7,0,0,0,0,6],[8,2,0,6,0,0,0,0,9],[0,3,0,0,0,0,5,8,0]]
    for y in range(0,9):
        for x in range(0,9):
            MatrixList[y][x] = int(string[counter])
            counter += 1
    return MatrixList

"""def print_numbers(board):
    for i, row in enumerate(board):
        for nums in row:
            if nums != 0:
                yield nums
            else:
                print(" ")"""

"""def print_nums(board):
    for i, row in enumerate(board):
            return tuple(x if x != 0 else " " for x in row)"""
       
    
def print_sudoku2(board):  # A board a mátrix!!
    letters = tuple(("A","B","C","D","E","F","G","H","I"))
    print(f"{Fore.BLUE}            " + "  1 " + "  2 " + "  3 " + "  4 " + "  5 " + "  6 " + "  7 " + "  8 " + "  9 " + f"  {Style.RESET_ALL}")
    print("            " + "┏" + "━━━┳"*8 + "━━━┓")
    for i, row in enumerate(board):
        print(f"{Fore.BLUE}          " + str(letters[i] + f"{Style.RESET_ALL} " + "┃" + " {} │ {} │ {} ┃"*3).format(*[str(x) if x != 0 else " " for x in row]))
        if i % 3 == 2:
            print("            " + "┣" + ("━━━┿"*2 + "━━━╋")*2 + "━━━┿"*2 + "━━━┫")
        elif i % 20 == 18:
            print("            " + "┗" + "━━━┻"*8 + "━━━┛")
        else:    
            print("            " + "┠" + ("───┼"*2 + "───╂")*2 + "───┼"*2 + "───┨")
    #print("            " + "┗" + "━━━┻"*8 + "━━━┛")

def user_input():
    while True:
        userinput = input("Enter the coordinates of the value you wish to change, followed by colon and the new value.\nFor example, 'A1:4'.\nPress q to quit game:  ").upper()
        if userinput == "q" or userinput == "Q": quit()
        if len(userinput) != 4:
            print("\nInvalid input, please try again!" + "\n" *2)
            continue
        ABC = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8}
        valid_numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        print(userinput[0])
        print(userinput[1])
        print(userinput[2])
        print(userinput[3])
        if (int(userinput[1]) not in valid_numbers[1:] 
        or int(userinput[3]) not in valid_numbers
        or userinput[0] not in list(ABC.keys())
        or userinput[2] != ":"):
            print("\nInvalid input, please try again!" + "\n" *2)
            continue
        x = int(ABC[userinput[0]])
        y = int(userinput[1])
        req_value = int(userinput[3])
        matrix_list_prod[x][y] = req_value
        update()        
        if check_validation():
            if check_verification():
                return True
        continue


def update():
    if platform.system() == 'Linux':
        os.system('clear')
        print(cont)
        print_sudoku2(matrix_list_prod)
    elif platform.system() == 'Windows':
        os.system('cls')
        print(cont)
        print_sudoku2(matrix_list_prod)      



def check_validation():
    ValidationCheck = 0  
    for i in range(0,9):
        if len(list(filter(lambda x: 10 > x > 0,matrix_list_prod[i]))) == 9:
            ValidationCheck += 1
        templist = [[i2][0] for i2 in range(0,9)]
        if len(list(filter(lambda x: 10 > x > 0,templist))):
            ValidationCheck += 1
    return True if ValidationCheck == 18 else False

def check_verification():
    check_verification = 0
    for i in range(0,9):
        if len(set(matrix_list_prod[i])) == len(matrix_list_prod[i]):
            check_verification += 1
        templist = [[i2][0] for i2 in range(0,9)]
        if len(set(templist)) == len(templist):
            check_verification += 1
    for block in range(0,7,3):
        for block2 in range(0,7,3):
            templist.clear()
            for i in range(0,3):
                for i2 in range(0,3):
                    templist.append(matrix_list_prod[i2 + block][i + block2])
            if len(set(templist)) == len(templist):
                check_verification += 1
    return True if check_verification == 27 else False

# A mátrix , a sudoku mezőinek értékeivel. Az értékek mátrix elemenként változtathatóak.

matrix_list_original = [\
[0,1,8,0,0,0,0,3,0],
[9,0,0,0,0,2,0,4,5],
[7,0,0,0,0,6,0,0,0],
[0,0,0,0,0,7,1,2,0],
[0,0,0,0,5,0,0,0,0],
[0,8,4,3,0,0,0,0,0],
[0,0,0,7,0,0,0,0,6],
[8,2,0,6,0,0,0,0,9],
[0,3,0,0,0,0,5,8,0]]

matrix_list_original = SudokuImport(1)
matrix_list_prod = SudokuImport(1) #"r" for random sudoku
#for Line in range(0,9):
    #print(MatrixList[Line])


"""Itt következik maga a sudoku tábla."""

print_sudoku2(matrix_list_prod)


"""A koordinatak a 9x9-es táblát A1-től I9-ig osztják fel. Egy harmadik inputtal a kivalasztott mátrix pontra lehet
    új értéket megadni , illetve javítani az előző értéken."""

# Koordinatak és új értékek:

while True:
    if user_input() == True:
        break

if platform.system() == 'Linux':
    os.system('clear')

elif platform.system() == 'Windows':
    os.system('cls')

    
print("Your winner!")

"""A győzelmi feltételek , illetve a helyes értékek ellenőrzése , eredmény megjelenítése"""

print("\n"*6)

        
