#----------------------------------------------
# Conway's Game of Life
# More programs at UsingPython.com/programs
#----------------------------------------------

import random
import time
import os
import platform
import copy

if platform.system() == 'Windows':
    CLEAR = 'cls'
else:
    CLEAR = 'clear'

#---------------------------------------------------------------------------

def initGrid(rows, cols, makingGen):
    for i in range(rows):
        makingGenRow = []
        for j in range(cols):
            if (i == 0 or j == 0 or (i == rows - 1) or (j == cols - 1)):
                makingGenRow += [-1]
            else:
                ran = random.randint(0,3)
                if ran == 0:
                    makingGenRow += [1]
                else:
                    makingGenRow += [0]
        makingGen += [makingGenRow]

#---------------------------------------------------------------------------
    
def printGen(rows, cols, makingGen, genNo):
    os.system(CLEAR)

    print("Game of Life -- Generation " + str(genNo) )
    
    for i in range(rows):
        for j in range(cols):
            if makingGen[i][j] == -1:
                print("#", end="")
            elif makingGen[i][j] == 1:
                print("O", end="")
            else:
                print(" ", end="")
        print("")

#---------------------------------------------------------------------------

def processNextGen(rows, cols, currentStatus, nextStatus):
    for i in range(1,rows-1):
        for j in range(1,cols-1):
            nextStatus[i][j] = processNeighbours(i, j, currentStatus)

#---------------------------------------------------------------------------
      
def processNeighbours(x, y, makingGen):
    nCount = 0
    for j in range(y-1,y+2):
        for i in range(x-1,x+2):
            if not(i == x and j == y):
                if makingGen[i][j] == 1:
                    nCount += makingGen[i][j]
    if makingGen[x][y] == 1 and nCount < 2:
        return 0
    if makingGen[x][y] == 1 and nCount > 3:
        return 0
    if makingGen[x][y] == 0 and nCount == 3:
        return 1
    else:
        return makingGen[x][y]

#---------------------------------------------------------------------------
############################################################################
