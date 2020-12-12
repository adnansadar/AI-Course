import numpy as np
import pandas as pd
a=[[0,0,0],[0,0,0],[0,0,0]]
b=np.array(a)
print("enter the elements of the matrix")
print("enter 2 for cross and 1 for O and O to keep blank")
blank=[]
zero=[]
cross=[]
x=0
temp=[]
mini=[]
maxi=[]
temp1=[]
array=np.zeros((9,9))
def winning(b,blank,cross,zero):
     for num in range(len(blank)):
        g,h=blank[num][0],blank[num][1]
        b[g][h]=1
        if(([g-1,h-1] in zero and [g+1,h+1] in zero) or ([g+1,h+1] in zero and [g+2,h+2] in zero) or ([g-1,h-1] in zero and [g-2,h-2] in zero)):
            mini.append([b,60])
            blank.pop(num)
            
        elif(([g,h+1] in zero and [g,h+2] in zero)or([g,h-1] in zero and [g,h+1] in zero)or([g,h-1] in zero and [g,h-2] in zero)or
             ([g+1,h] in zero and [g+2,h] in zero)or([g-1,h] in zero and [g+1,h] in zero)or([g-1,h] in zero and [g-2,h] in zero)):
            mini.append([b,60])
            blank.pop(num)
        else:
            b[g][h]=0
     #return blank
for i in range(3):
    for j in range(3):
        e=int(input())
        if((e==0 or e==2 or e==1)):
            if(e==0):
                blank.append([i,j])
            elif(e==1):
                zero.append([i,j])
            elif(e==2):
                cross.append([i,j])
        array[0][x]=e
        temp.append(e)
        x=x+1
            
        b[i][j]=e
#print("blank",blank)
print("\nThe original matrix is""\n",b)
#blank=winning(b,blank,cross,zero)
winning(b,blank,cross,zero)
def calculate(b,blank,cross,zero):
    temp1=[b]
    m=[]
    for num in range(len(blank)):
        g,h=blank[num][0],blank[num][1]
        b[g][h]=2
        print("\n")
        print("One possible move can be""\n",b)
        if(([g-1,h-1] in cross and [g+1,h+1] in cross) or ([g+1,h+1] in cross and [g+2,h+2] in cross) or ([g-1,h-1] in cross and [g-2,h-2] in cross)):
            #print("Winning, The score is 60")
            #if(m>-60):
             #   m=-60
            m.append(-60)
            #temp1.append(m)
            
        elif(([g,h+1] in cross and [g,h+2] in cross)or([g,h-1] in cross and [g,h+1] in cross)or([g,h-1] in cross and [g,h-2] in cross)or
         ([g+1,h] in cross and [g+2,h] in cross)or([g-1,h] in cross and [g+1,h] in cross)or([g-1,h] in cross and [g-2,h] in cross)):
            #print("Winning, The score is 60")
           # if(m>-60):
             #   m=-60
            m.append(-60)
        elif(([g-1,h-1] in zero and [g+1,h+1] in zero) or ([g+1,h+1] in zero and [g+2,h+2] in zero) or ([g-1,h-1] in zero and [g-2,h-2] in zero)):
            #print("Blocking, The score is 50")
            #if(m>-50):
             #   m=-50
            m.append(-50)
        elif(([g,h+1] in zero and [g,h+2] in zero) or ([g,h-1] in zero and [g,h+1] in zero) or ([g,h-1] in zero and [g,h-2] in zero)or
         ([g+1,h] in zero and [g+2,h] in zero)or([g-1,h] in zero and [g+1,h] in zero)or([g-1,h] in zero and [g-2,h] in zero)):
            #print("Blocking, The score is 50")
            #if(m>-50):
             #   m=-50
            m.append(-50)
            
        elif(g==1 and h==1):
            #print("Else Case,The score is 4")
            #if(m>--4):
            #    m=-4
            m.append(-4)
        
        elif((g+h)%2==0):
            #print("Else Case,The score is 3")
            #if(m>-3):
            #    m=-3
            m.append(-3)
        else:
            #print("Else Case,The score is 2")
            #if(m>-2):
             #   m=-2
            m.append(-2)
        b[g][h]=0
    temp1.append(min(m))
    print("The scores are \n",m,'\n')
    print("\nThe chosen value is ",min(m),"\n")
    mini.append(temp1)
def new(array):
    blank,zero,cross=[],[],[]
    for i in range(3):
        for j in range(3):
            if(array[i,j]==0):
                blank.append([i,j])
            elif(array[i,j]==1):
                zero.append([i,j])
            elif(array[i,j]==2):
                cross.append([i,j])
    calculate(array,blank,cross,zero)
            
for i in range(len(blank)):
    array[i][0:9]=temp
    if(blank[i][0]==0):
        array[i][blank[i][1]]=1
    elif(blank[i][0]==1):
        array[i][(blank[i][1])+3]=1
    else:
        array[i][blank[i][1]+6]=1
    print("Calculating moves for\n",np.array(array[i][:]).reshape(3,3))
    new(np.array(array[i][:]).reshape(3,3))
print("mini",*mini,sep="\n")
temp=np.array(temp).reshape(3,3)
#print("temp\n",temp)
l=0
for i in range(len(mini)):
    if(mini[l][1]<mini[i][1]):
        l=i
    
for i in range(3):
    for j in range(3):
        if(temp[i,j]!=mini[l][0][i,j]):
            print("\nBest Location",i,",",j)
print("\nThe Best Move possible is \n",mini[l])
#print("\n Possible move generator is\n",array)