N = 7
K = [[0,2],[0,4],
        [0,5],[1,2],
        [1,3],[1,5],
        [2,3],[2,4],
        [2,5],[4,6]]
L = [[2,4,5], [2,3,5], [0,1,3,4,5], [1,2], [0,2,6], [0,1,2],  [4]]

A = [
    [0,0,1,0,1,1,0],
    [0,0,1,1,0,1,0],
    [1,1,0,1,1,1,0],
    [0,1,1,0,0,0,0],
    [1,0,1,0,0,0,1],
    [1,1,1,0,0,0,0],
    [0,0,0,0,1,0,0]
    ]
def einsa():
    print("einsa")
    print(len(K))

def einsb():
    print("einsb")
    number=0
    for i in range(len(L)):
        number = number + len(L[i])
    print(str(number/2))

def einsc():
    print("einsc")
    num=0
    for i in range(len(A)):
        num = num + sum(A[i])
    print(num/2)

def zweia():
    print("zweia")
    A=int(input())
    B=int(input())
    if ([A,B] in K or [B,A] in K):
        print(str(A) + "-" + str(B)+ " ist Kante")
        return
    print("Keine Kante")

def zweib():
    print("zweib")
    A=int(input())
    B=int(input())
    if(B in L[A]):
        print(str(A) + "-" + str(B)+ " ist Kante")
        return
    print("Keine Kante")


def zweic():
    print("zweic")
    AA=int(input())
    B=int(input())
    if(A[AA][B] ==1):
        print(str(AA) + "-" + str(B)+ " ist Kante")
        return
    print("Keine Kante")
    
def drei():
    print("drei")
    AListe =[]
    for i in range(N):
        AListe.append([])
    for i in range(N):
        for j in range(len(K)):
            if(K[j][0]==i):
                AListe[i].append(K[j][1])
                AListe[K[j][1]].append(i)
    print(AListe)

def vier():
    print("vier")
    AMatrix=[]
    for i in range(N):
        AMatrix.append([])
        for j in range(N):
            if (j in L[i]):
                 AMatrix[i].append(1)
            else:
                AMatrix[i].append(0)
    print(AMatrix)


def fuenf():
    print("fuenf")
    LKnots=[]
    for i in range(N):
        for j in range(N):
            if (A[i][j] == 1):
                if ([i,j] not in LKnots and [j,i] not in LKnots):
                    LKnots.append([i,j])

    print(LKnots)

    
einsa()
einsb()
einsc()
zweia()
zweib()
zweic()
drei()
vier()
fuenf()
