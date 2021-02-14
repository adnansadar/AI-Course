from collections import OrderedDict
import numpy as np

openlist = {}
closedlist = {}
initialstate = []
goalstate = [0, 2, 3, 8, 4, 1, 7, 6, 5]
totalmoves = []
# {0 2 3}
# {8 4 1}
# {7 6 5}


def main():
    global openlist
    global closedlist
    global initialstate
    global goalstate
    global totalmoves

    print("GOAL STATE:\n", goalstate)
    print("\nEnter input matrix:")
    for i in range(9):  # taking inital state input from user
        no = int(input())
        initialstate.append(no)
        if(no == 0):
            emptycellindex = i  # store the index of empty cell
    print("INITIAL STATE:\n", initialstate)
    print("***************************************************************************")
    totalmoves = [[0 for col in range(9)]
                  for row in range(4)]  # initializing array with zeros
    # storing initial state in totalmoves array
    totalmoves[0][:] = initialstate
    # initially current state has no father and child nodes
    heuristicfunction(totalmoves, 1, None)
    movegenerator(initialstate)
    bestpath(closedlist)


def heuristicfunction(totalmoves, c, father):
    for i in range(c):
        heuristicvalue = 0
        for j in range(9):
            if(totalmoves[i][j] != goalstate[j]):  # check if its a misplaced tile
                heuristicvalue += 1  # increment heuristic value for that move
        # store copy of totalmoves in temparr
        temparr = totalmoves[i][:].copy()
        # join using comma as a seperator
        temp = (",".join(str(element) for element in temparr))
        # store heuristic value and father matrix of that move in openlist
        openlist[temp] = [heuristicvalue, father]
    initializelinkedlist(openlist)


def initializelinkedlist(openlist):
    print("\nOPENLIST(Current State : [Heuristic Value, Father]):\n", openlist)
    # sorting based on heuristic value(key)
    temparr = sorted(openlist.items(), key=lambda k: k[1][0])
    var = temparr[0][0]
    # maintains the order of the openlist
    openlist = OrderedDict(sorted(openlist.items(), key=lambda k: k[1][0]))
    closedlist[var] = openlist[var]
    print(
        "CLOSEDLIST(Current State : [Heuristic Value, Father]):\n", closedlist)
    print("\n********************************************************************************")
    # the first element in the openlist has the least heuristic value
    minimumheuristic = openlist[var][0]
    arr = list(map(int, var.split(",")))
    # remove the element with least heuristic value from openlist
    del(openlist[var])
    if(minimumheuristic != 0):  # check if its not the goal state
        movegenerator(arr)


def movegenerator(beststate):
    for i in range(9):  # finding empty cell index
        if(beststate[i] == 0):
            emptycellindex = i
    if(emptycellindex == 4):  # center case
        possiblemoves = [1, 3, 5, 7]
        for i in range(4):
            x = possiblemoves[i]
            totalmoves[i][:] = beststate
            # switching empty cell position of current state and new state
            totalmoves[i][emptycellindex] = beststate[x]
            totalmoves[i][x] = 0
        # current move has 4 child nodes, they will be added to the openlist
        heuristicfunction(totalmoves, 4, beststate)

    elif(emptycellindex == 1 or emptycellindex == 3 or emptycellindex == 5 or emptycellindex == 7):
        if(emptycellindex == 3 or emptycellindex == 5):
            possiblemoves = [emptycellindex-3, emptycellindex+3, 4]
        if(emptycellindex == 1 or emptycellindex == 7):
            possiblemoves = [emptycellindex-1, emptycellindex+1, 4]
        for i in range(3):
            x = possiblemoves[i]
            totalmoves[i][:] = beststate
            totalmoves[i][emptycellindex] = beststate[x]
            totalmoves[i][x] = 0
        heuristicfunction(totalmoves[:][:], 3, beststate)

    else:  # edge case
        if(emptycellindex == 6 or emptycellindex == 8):
            possiblemoves = [emptycellindex-3, 7]
        if(emptycellindex == 0 or emptycellindex == 2):
            possiblemoves = [1, emptycellindex+3]
        for i in range(2):
            x = possiblemoves[i]
            totalmoves[i][:] = beststate
            totalmoves[i][emptycellindex] = beststate[x]
            totalmoves[i][x] = 0
        heuristicfunction(totalmoves, 2, beststate)


def bestpath(closedlist):
    print("Best Path Chosen by the Algorithm:")
    cost = 0
    for i in closedlist:
        current = list(map(int, i.split(",")))
        current = np.array(current)
        if(closedlist[i][1] != None):  # check if father is none
            fathernode = np.array(closedlist[i][1]).reshape(3, 3)  # store
        else:
            fathernode = None
        cost += 1
        print("Path Cost: 1")
        print("Heuristic value:", closedlist[i][0])
        print(current.reshape(3, 3), "\nFather:-\n", fathernode, "\n")
    print("Goal state reached!(Heuristic Value is 0)")
    print("Total cost of reaching goal state:", cost)


if __name__ == "__main__":
    main()
