import numpy as np
import math
from collections import OrderedDict
c = []
opend = {}
closed = {}


def calculate(moves, c, father):
    for j in range(c):
        d = 0
        for i in range(9):
            if(moves[j][i] != array1[i]):
                d = d+1
        temp = list(moves[j][:])
        temp1 = (",".join(str(ele) for ele in temp))
        opend[temp1] = [d, father]
        # print(moves[j][:].reshape(3,3),"\n",d,"\n")
    # print(opend)
    linked(opend)


def linked(opend):
    print("open\n", opend)
    temp2 = sorted(opend.items(), key=lambda k: k[1][0])
    var = temp2[0][0]
    opend = OrderedDict(sorted(opend.items(), key=lambda k: k[1][0]))
    closed[var] = opend[var]
    print("\nclosed\n", closed)
    minimum = opend[var][0]
    ar = list(map(float, var.split(",")))
    del(opend[var])
    if(minimum != 0):
        pmoves(ar)


def pmoves(array2):
    for i in range(9):
        if(array2[i] == 0):
            b = i
    if(b in [0, 2, 6, 8]):
        if(b == 8 or b == 6):
            p = [b-3, 7]
        if(b == 2 or b == 0):
            p = [1, b+3]
        for i in range(2):
            x = p[i]
            moves[i][:] = array2
            moves[i][b] = array2[x]
            moves[i][x] = 0
        calculate(moves, 2, array2)
    elif(b == 4):
        p = [1, 3, 5, 7]
        for i in range(4):
            x = p[i]
            moves[i][:] = array2
            moves[i][b] = array2[x]
            moves[i][x] = 0
        calculate(moves, 4, array2)
    else:
        if(b == 3 or b == 5):
            p = [b-3, b+3, 4]
        if(b == 1 or b == 7):
            p = [b-1, b+1, 4]
        for i in range(3):
            x = p[i]
            moves[i][:] = array2
            moves[i][b] = array2[x]
            moves[i][x] = 0
        calculate(moves[:][:], 3, array2)


array1 = np.array([1, 2, 3, 8, 0, 4, 7, 6, 5])
print("The goal matrix is\n", array1.reshape(3, 3))
array2 = []
moves = np.zeros((4, 9))
for i in range(9):
    a = int(input())
    array2.append(a)
    if(a == 0):
        b = i
print(array2)
moves[0][:] = array2
calculate(moves, 1, None)
pmoves(array2)

# print(opend)
# print("ans",closed)
print("\n")
cost = 0
for i in closed:
    temp3 = list(map(float, i.split(",")))
    temp3 = np.array(temp3)
    if(closed[i][1] != None):
        temp4 = np.array(closed[i][1]).reshape(3, 3)
    else:
        temp4 = None
    cost = cost+1
    print(temp3.reshape(3, 3), "Heuristic value:-",
          closed[i][0], "\nFather:-\n", temp4, "\n")
print("Goal state reached")
print("Total cost", cost)
