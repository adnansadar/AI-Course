import numpy as np
temparr2=np.array([[0,0,0],[0,0,0],[0,0,0]])
emptyarr=[]
noughtarr=[]
crossarr=[]
minimizingarr=[]
inputarray=np.zeros((9,9))

def main():
    global inputarray
    global emptyarr
    global noughtarr
    global crossarr
    global temparr2
    global minimizingarr
    k = 0
    temparr1=[]
    print("*******************************TIC-TAC-TOE USING MINIMAX******************************************")
    print("Enter the current board position:")
    print("2 for o and 1 for x and O for blank space")
    # {x o  }
    # {o x o}
    # {  x  }
    # o's turn now
    for i in range(3):
        for j in range(3):
            userinput=int(input())
            if((userinput==0 or userinput==1 or userinput==2)):
                if(userinput==0):
                    emptyarr.append([i,j])
                elif(userinput==2):
                    noughtarr.append([i,j])
                elif(userinput==1):
                    crossarr.append([i,j])
            inputarray[0][k]=userinput
            temparr1.append(userinput)
            k+=1
                
            temparr2[i][j]=userinput
    #print("emptyarr",emptyarr)
    print("\nCurrent Board Position: \n",temparr2)
    print("******************************************************************************")
    #emptyarr=winning(temparr2,emptyarr,crossarr,noughtarr)
    winning(temparr2,emptyarr,crossarr,noughtarr)
    
    for i in range(len(emptyarr)):
        inputarray[i][0:9]=temparr1
        if(emptyarr[i][0]==0):
            inputarray[i][emptyarr[i][1]]=2
        elif(emptyarr[i][0]==2):
            inputarray[i][(emptyarr[i][1])+3]=2
        else:
            inputarray[i][emptyarr[i][1]+6]=2
        print("Calculating moves for\n",np.array(inputarray[i][:]).reshape(3,3))
        new(np.array(inputarray[i][:]).reshape(3,3))

    print("minimizingarr",*minimizingarr,sep="\n")
    temparr1=np.array(temparr1).reshape(3,3)
    #print("temparr1\n",temparr1)
    l=0
    for i in range(len(minimizingarr)):
        if(minimizingarr[l][1]<minimizingarr[i][1]):
            l=i
        
    for i in range(3):
        for j in range(3):
            if(temparr1[i,j]!=minimizingarr[l][0][i,j]):
                print("\nBest Location",i,",",j)
    print("\nThe Best Move possible is \n",minimizingarr[l])
    #print("\n Possible move generator is\n",inputarray)

def winning(temparr2,emptyarr,crossarr,noughtarr):
     for num in range(len(emptyarr)):
        g,h=emptyarr[num][0],emptyarr[num][1]
        temparr2[g][h]=2
        if(([g-1,h-1] in noughtarr and [g+1,h+1] in noughtarr) or ([g+1,h+1] in noughtarr and [g+2,h+2] in noughtarr) or ([g-1,h-1] in noughtarr and [g-2,h-2] in noughtarr)):
            minimizingarr.append([temparr2,60])
            emptyarr.pop(num)
            
        elif(([g,h+1] in noughtarr and [g,h+2] in noughtarr)or([g,h-1] in noughtarr and [g,h+1] in noughtarr)or([g,h-1] in noughtarr and [g,h-2] in noughtarr)or
             ([g+1,h] in noughtarr and [g+2,h] in noughtarr)or([g-1,h] in noughtarr and [g+1,h] in noughtarr)or([g-1,h] in noughtarr and [g-2,h] in noughtarr)):
            minimizingarr.append([temparr2,60])
            emptyarr.pop(num)
        else:
            temparr2[g][h]=0
     #return emptyarr

def calculate(temparr2,emptyarr,crossarr,noughtarr):
    temp1=[]
    temp1=[temparr2]
    m=[]
    for num in range(len(emptyarr)):
        g,h=emptyarr[num][0],emptyarr[num][1]
        temparr2[g][h]=1
        print("\n")
        print("One possible move can be""\n",temparr2)
        if(([g-1,h-1] in crossarr and [g+1,h+1] in crossarr) or ([g+1,h+1] in crossarr and [g+2,h+2] in crossarr) or ([g-1,h-1] in crossarr and [g-2,h-2] in crossarr)):
            #print("Winning, The score is 60")
            #if(m>-60):
             #   m=-60
            m.append(-60)
            #temp1.append(m)
            
        elif(([g,h+1] in crossarr and [g,h+2] in crossarr)or([g,h-1] in crossarr and [g,h+1] in crossarr)or([g,h-1] in crossarr and [g,h-2] in crossarr)or
         ([g+1,h] in crossarr and [g+2,h] in crossarr)or([g-1,h] in crossarr and [g+1,h] in crossarr)or([g-1,h] in crossarr and [g-2,h] in crossarr)):
            #print("Winning, The score is 60")
           # if(m>-60):
             #   m=-60
            m.append(-60)
        elif(([g-1,h-1] in noughtarr and [g+1,h+1] in noughtarr) or ([g+1,h+1] in noughtarr and [g+2,h+2] in noughtarr) or ([g-1,h-1] in noughtarr and [g-2,h-2] in noughtarr)):
            #print("Blocking, The score is 50")
            #if(m>-50):
             #   m=-50
            m.append(-50)
        elif(([g,h+1] in noughtarr and [g,h+2] in noughtarr) or ([g,h-1] in noughtarr and [g,h+1] in noughtarr) or ([g,h-1] in noughtarr and [g,h-2] in noughtarr)or
         ([g+1,h] in noughtarr and [g+2,h] in noughtarr)or([g-1,h] in noughtarr and [g+1,h] in noughtarr)or([g-1,h] in noughtarr and [g-2,h] in noughtarr)):
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
        temparr2[g][h]=0
    temp1.append(min(m))
    print("The scores are \n",m,'\n')
    print("\nThe chosen value is ",min(m),"\n")
    minimizingarr.append(temp1)
def new(inputarray):
    emptyarr,noughtarr,crossarr=[],[],[]
    for i in range(3):
        for j in range(3):
            if(inputarray[i,j]==0):
                emptyarr.append([i,j])
            elif(inputarray[i,j]==2):
                noughtarr.append([i,j])
            elif(inputarray[i,j]==1):
                crossarr.append([i,j])
    calculate(inputarray,emptyarr,crossarr,noughtarr)

if __name__ == "__main__":
    main()
