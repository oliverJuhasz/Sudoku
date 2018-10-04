
MatrixList = [
[1,8,4,9,6,3,7,2,5],
[5,6,2,7,4,8,3,1,9],
[3,9,7,5,1,2,8,6,4],
[2,3,9,6,5,7,1,4,8],
[7,5,6,1,8,4,2,9,3],
[4,1,8,2,3,9,6,5,7],
[9,4,1,3,7,6,5,8,2],
[6,2,3,8,9,5,4,7,1],
[8,7,5,4,2,1,9,3,6]]

print(*MatrixList,sep="\n")

def color_checker(board,x,y):
    checked_number = board[x][y]
    templist = []
    
    #horizontal check
    if board[x].count(checked_number) > 1:
        print("Horizontal duplication")
    #vertical check
    templist = list(board[i][0] for i in range(0,9))
    if templist.count(checked_number) > 1:
        print("Vertical duplication")
    #block check
    templist = []
    blockIDx = 0
    blockIDy = 0
    if x < 4:
        blockIDx = 0
    elif x < 7:
        blockIDx = 3
    elif x < 10:
        blockIDx = 6
    if y < 4:
        blockIDy = 0
    elif y < 7:
        blockIDy = 3
    elif y < 10:
        blockIDy = 6    
    for i in range(0 + blockIDy, 3 + blockIDy):
        for i2 in range(0 + blockIDx, 3 + blockIDx):
            templist.append(board[i][i2])
    if templist.count(checked_number) > 1:
        print("Block duplication")


color_checker(MatrixList,1,8)