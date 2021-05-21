import io,os,sys

# # # input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
sys.stdin = open("OChu.txt","r")
sys.stdout = open("OChu_1.txt","w")



String = input()
a = []
while True:
    x = (input())
    if x[0]==".":
        break
    else :
        a.append(list(x))
def Xuli(a,String):
    Start = []
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]==String[0]:
                Start.append((i,j))
    dx = [0,1,0,-1,-1,1,-1,1]
    dy = [1,0,-1,0,-1,1,1,-1]
    DoDai= 0 
    Check = 1
    while  DoDai < len(Start):
        x, y = Start[DoDai][0],Start[DoDai][1]
        stack = []
        stack.append((x,y))
        path = []
        path.append((x,y))
        kq =[]
        while len(stack) !=0 :
            s = stack.pop()
            if len(path) == len(String): 
                print("true")
                print(*path)
                print(String)
                return
            VT = []
            for i in range(8):
                VT1 = s[0] + dx[i]
                VT2 = s[1] + dy[i]
                if 0<= VT1 and VT1<len(a) and 0<=VT2 and VT2<len(a[0]) :
                    VT.append((VT1,VT2))
            while VT :
                x = VT.pop()
                
                if a[x[0]][x[1]] == String[len(path)] and  x not in path:
                    path.append(x)
                    stack.append(x)
                    break

        DoDai+=1

    print("false")

Xuli(a,String)
        


                    
# ABCB
# ABCE
# SFCS
# ADEE
# .