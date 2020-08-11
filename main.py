#---------------------------------------------------------------------------
#importing the packages containing neccesaary functions and initializers
from GameOfLife import *
from GameParameters import *

#declaring two empty lists for further use
thisGen = []
nextGen = []

#calling the initGrid function to intialise the thisGen list
initGrid(ROWS, COLS,  thisGen)

#using deepcopy function to create a copy of thisGen list into nextGen for performing changes without affecting the original list i.e. thisGen
nextGen = copy.deepcopy(thisGen)

#calling the printGen function to print the board for the actions
printGen(ROWS, COLS, thisGen, 0)

#looping through generations 
for gens in range(1, GENERATIONS+1):
    input("1Press ENTER to see next generation")
    #calling processNextGen function for processing the next generation 
    processNextGen(ROWS, COLS, thisGen, nextGen)
    printGen(ROWS, COLS, nextGen, gens)
    thisGen = copy.deepcopy(nextGen)
input("Finished. Press ENTER to quit.")

