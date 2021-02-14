import numpy as np
temparr2 = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
emptyarr = []
noughtarr = []
crossarr = []
minimizingarr = []
possiblemovesarr = np.zeros((9, 9))


def main():
    global possiblemovesarr
    global noughtarr
    global emptyarr
    global crossarr
    global minimizingarr
    global temparr2

    temparr1 = []
    k = 0
    print("*******************************TIC-TAC-TOE USING MINIMAX******************************************")
    print("Enter the current board position:")
    print("2 for x and 1 for o and O for blank space")
    # {x o  }
    # {o x o}
    # {  x  }
    # o's turn now
    for i in range(3):
        for j in range(3):
            userinput = int(input())
            if((userinput == 0 or userinput == 2 or userinput == 1)):
                if(userinput == 2):
                    crossarr.append([i, j])
                elif(userinput == 1):
                    noughtarr.append([i, j])
                elif(userinput == 0):
                    emptyarr.append([i, j])
            possiblemovesarr[0][k] = userinput
            temparr1.append(userinput)
            k += 1
            temparr2[i][j] = userinput

    print("\nCurrent Board Position: \n", temparr2)
    print("******************************************************************************")
    checkwin(temparr2, emptyarr, crossarr, noughtarr)

    for i in range(len(emptyarr)):
        possiblemovesarr[i][0:9] = temparr1
        if(emptyarr[i][0] == 0):
            possiblemovesarr[i][emptyarr[i][1]] = 1  # 1=0
        elif(emptyarr[i][0] == 1):
            possiblemovesarr[i][(emptyarr[i][1])+3] = 1
        else:
            possiblemovesarr[i][emptyarr[i][1]+6] = 1
        print("Possible moves for Board Position:\n",
              np.array(possiblemovesarr[i][:]).reshape(3, 3))
        updatearr(np.array(possiblemovesarr[i][:]).reshape(3, 3))
    print("The Minimizing Array(after 2 ply search):", *minimizingarr, sep="\n")
    temparr1 = np.array(temparr1).reshape(3, 3)
    m = 0
    for i in range(len(minimizingarr)):  # finding best move
        if(minimizingarr[m][1] < minimizingarr[i][1]):
            m = i
    print("****************************************************************************")
    print("\nThe Best Move for o is: \n", minimizingarr[m])


def checkwin(userinput, emptyarr, crossarr, noughtarr):
    for num in range(len(emptyarr)):  # len=3
        g, h = emptyarr[num][0], emptyarr[num][1]
        # 1=o inserting o at the first empty pos in currentboard
        userinput[g][h] = 1
        # checking all wining positions in  diagonals
        if(([g-1, h-1] in noughtarr and [g+1, h+1] in noughtarr) or ([g+1, h+1] in noughtarr and [g+2, h+2] in noughtarr) or ([g-1, h-1] in noughtarr and [g-2, h-2] in noughtarr)):
            # display board position and score
            minimizingarr.append([userinput, 60])
            emptyarr.pop(num)  # removing move from emptyarr

        # checking all wining positions in rows,columns
        elif(([g, h+1] in noughtarr and [g, h+2] in noughtarr) or ([g, h-1] in noughtarr and [g, h+1] in noughtarr) or ([g, h-1] in noughtarr and [g, h-2] in noughtarr) or
             ([g+1, h] in noughtarr and [g+2, h] in noughtarr) or ([g-1, h] in noughtarr and [g+1, h] in noughtarr) or ([g-1, h] in noughtarr and [g-2, h] in noughtarr)):
            minimizingarr.append([userinput, 60])
            emptyarr.pop(num)
        else:  # if no winning position
            userinput[g][h] = 0


def minimizingmoves(temparr2, emptyarr, crossarr, noughtarr):
    temp1 = [temparr2]
    m = []
    for num in range(len(emptyarr)):
        g, h = emptyarr[num][0], emptyarr[num][1]
        temparr2[g][h] = 2
        print("\n")
        print("Possible Move ", num+1)
        print("\n", temparr2)
        # minimizing diagonal winning
        if(([g-1, h-1] in crossarr and [g+1, h+1] in crossarr) or ([g+1, h+1] in crossarr and [g+2, h+2] in crossarr) or ([g-1, h-1] in crossarr and [g-2, h-2] in crossarr)):
            m.append(-60)

        # minimizing row/column winning
        elif(([g, h+1] in crossarr and [g, h+2] in crossarr) or ([g, h-1] in crossarr and [g, h+1] in crossarr) or ([g, h-1] in crossarr and [g, h-2] in crossarr) or
             ([g+1, h] in crossarr and [g+2, h] in crossarr) or ([g-1, h] in crossarr and [g+1, h] in crossarr) or ([g-1, h] in crossarr and [g-2, h] in crossarr)):
            m.append(-60)

        # minimizing diagonal blocking
        elif(([g-1, h-1] in noughtarr and [g+1, h+1] in noughtarr) or ([g+1, h+1] in noughtarr and [g+2, h+2] in noughtarr) or ([g-1, h-1] in noughtarr and [g-2, h-2] in noughtarr)):
            m.append(-50)

        # minimizing row/column blocking
        elif(([g, h+1] in noughtarr and [g, h+2] in noughtarr) or ([g, h-1] in noughtarr and [g, h+1] in noughtarr) or ([g, h-1] in noughtarr and [g, h-2] in noughtarr) or
             ([g+1, h] in noughtarr and [g+2, h] in noughtarr) or ([g-1, h] in noughtarr and [g+1, h] in noughtarr) or ([g-1, h] in noughtarr and [g-2, h] in noughtarr)):
            m.append(-50)

        # else center condition
        elif(g == 1 and h == 1):
            m.append(-4)

        # else middle condition
        elif((g+h) % 2 == 0):
            m.append(-3)

        # else corner condition
        else:
            m.append(-2)
        temparr2[g][h] = 0
    # appending the best move(minimum) for minimizing player
    temp1.append(min(m))
    print("\n")
    for i in m:
        print("Score:", i)
    # print("\nThe scores are \n", m, '\n')
    print("\nThe value chosen(best) by minimizing player is ", min(m), "\n")
    print("*********************************************************************\n")
    minimizingarr.append(temp1)


def updatearr(possiblemovesarr):
    emptyarr, noughtarr, crossarr = [], [], []
    for i in range(3):
        for j in range(3):
            if(possiblemovesarr[i, j] == 0):
                emptyarr.append([i, j])
            elif(possiblemovesarr[i, j] == 1):
                noughtarr.append([i, j])
            elif(possiblemovesarr[i, j] == 2):
                crossarr.append([i, j])
    minimizingmoves(possiblemovesarr, emptyarr, crossarr, noughtarr)


if __name__ == "__main__":
    main()
