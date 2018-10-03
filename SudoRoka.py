import os
import platform
import random
import time
from colorama import init
from colorama import Fore, Back, Style
   

def color_generator(board):
    colortrix = [[1,8,4,9,6,3,7,2,5],[5,6,2,7,4,8,3,1,9],[3,9,7,5,1,2,8,6,4],[2,3,9,6,5,7,1,4,8],[7,5,6,1,8,4,2,9,3],[4,1,8,2,3,9,6,5,7],[9,4,1,3,7,6,5,8,2],[6,2,3,8,9,5,4,7,1],[8,7,5,4,2,1,9,3,6]]
    for i, elem in enumerate(board):
        for i2, subelem in enumerate(elem):
            if subelem == 1:
                colortrix[i][i2] = f"{Fore.CYAN}1{Style.RESET_ALL}"
            elif subelem == 2:
                colortrix[i][i2] = f"{Fore.RED}2{Style.RESET_ALL}"                
            elif subelem == 3:
                colortrix[i][i2] = f"{Fore.GREEN}3{Style.RESET_ALL}"     
            elif subelem == 4:
                colortrix[i][i2] = f"{Fore.YELLOW}4{Style.RESET_ALL}"    
            elif subelem == 5:
                colortrix[i][i2] = f"{Fore.BLUE}5{Style.RESET_ALL}"    
            elif subelem == 6:
                colortrix[i][i2] = f"{Fore.MAGENTA}6{Style.RESET_ALL}"    
            elif subelem == 7:
                colortrix[i][i2] = f"{Fore.WHITE}7{Style.RESET_ALL}"    
            elif subelem == 8:
                colortrix[i][i2] = f"{Fore.BLUE}8{Style.RESET_ALL}"                                                                            
            elif subelem == 9:
                colortrix[i][i2] = f"{Fore.GREEN}9{Style.RESET_ALL}"                    
            else:
                colortrix[i][i2] = " "                  
    return colortrix
    
MatrixList = [[1,8,4,9,6,3,7,2,5],[5,6,2,7,4,8,3,1,9],[3,9,7,5,1,2,8,6,4],[2,3,9,6,5,7,1,4,8],[7,5,6,1,8,4,2,9,3],[4,1,8,2,3,9,6,5,7],[9,4,1,3,7,6,5,8,2],[6,2,3,8,9,5,4,7,1],[8,7,5,4,2,1,9,3,6]]
colorstring = ""
color = color_generator(MatrixList)

for elem in color:
    colorstring = ""
    for subelem in elem:
        colorstring += subelem
    print(colorstring)



#list(sorted(inventory.items(), key=lambda x: x[1],reverse=False))