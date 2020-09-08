import numpy as np
a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
inputarr = np.array(a)
print("Enter the elements of the matrix")
print("Enter 2 for X, 1 for O and 0 to leave blank")
blankarr = []
zeroarr = []
crossarr = []
d = 1
x = 0
temp = []
array = np.zeros((9, 9))
# print(array)
for i in range(3):
    for j in range(3):
        userinput = int(input())
        # while(userinput != 0 or userinput != 1 or userinput != 2):
        #     print("Please enter again!")
        #     userinput = int(input())
        #     break
        if(userinput == 0):
            blankarr.append([i, j]) #save index location
        elif(userinput == 1):
            zeroarr.append([i, j])  #save index location
        elif(userinput == 2):
            crossarr.append([i, j])  # save index location
        array[0][x] = userinput 
        temp.append(userinput)
        x += 1

        inputarr[i][j] = userinput  # Enter the input in the matrix
        d += 1
print(blankarr)
print("The matrix entered is:""\n", inputarr)
for i in range(len(blankarr)):
    array[i][0:] = temp
    if(blankarr[i][0] == 0):
        array[i][blankarr[i][1]] = 2
    elif(blankarr[i][0] == 1):
        array[i][(blankarr[i][1])+3] = 2
    else:
        array[i][blankarr[i][1]+6] = 2

print(array)

for num in range(len(blankarr)):
    g, h = blankarr[num][0], blankarr[num][1]
    inputarr[g][h] = 2
    print("The matrix after playing move is""\n", inputarr)
    if(([g-1, h-1] in crossarr and [g+1, h+1] in crossarr) or ([g+1, h+1] in crossarr and [g+2, h+2] in crossarr) or ([g-1, h-1] in crossarr and [g-2, h-2] in crossarr)):
        print("Winning: The score is 60")

    elif(([g, h+1] in crossarr and [g, h+2] in crossarr) or ([g, h-1] in crossarr and [g, h+1] in crossarr) or ([g, h-1] in crossarr and [g, h-2] in crossarr)):
        print("Winning: The score is 60")
    elif(([g-1, h-1] in zeroarr and [g+1, h+1] in zeroarr) or ([g+1, h+1] in zeroarr and [g+2, h+2] in zeroarr) or ([g-1, h-1] in zeroarr and [g-2, h-2] in zeroarr)):
        print("Blocking, The score is 50")
    elif(([g, h+1] in zeroarr and [g, h+2] in zeroarr) or ([g, h-1] in zeroarr and [g, h+1] in zeroarr) or ([g, h-1] in zeroarr and [g, h-2] in zeroarr)):
        print("Blocking: The score is 50")
    elif(g == 1 and h == 1):
        print("Else Case: The score is 4")

    elif((g+h) % 2 == 0):
        print("Else Case: The score is 3")
    else:
        print("Else Case: The score is 2")
    inputarr[g][h] = 0
