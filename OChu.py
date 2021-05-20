# import io,os,sys
# # input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# sys.stdin = open("OChu.txt","r")
# sys.stdout = open("OChu_1.txt","w")
String = input()
a = []
while True:
    x = input()
    if x[0]=='.':
        break
    else :
        a.append(x)
Start = []
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j]==String[0]:
            Start.append((i,j))
dx = [0,1,0,-1]
dy = [1,0,-1,0]
DoDai= 0 
Check = 1
while  DoDai < len(Start):
    x, y = Start[DoDai][0],Start[DoDai][1]
    i = 1 
    DoDai +=1
    DanhDau = [[0]*len(a[0])] * len(a)
    DanhDau[x][y] = 1
    while i < len(String):
        k = 0 
        while k < 4:
            New_x = x + dx[k]
            New_y = y + dy[k]
            if New_x >=0 and New_y >= 0 and New_x < len(a[0]) and New_y < len(a) and DanhDau[x][y] == 0  :
                if a[New_x][New_y] == String[i]  : 
                    i+=1
                    print("{} ----- {} -----".format(x,y))
                    print("_________" + str(i))
                    DanhDau[New_x][New_y]=1
                    x = New_x
                    y = New_y
                    break
                
            k+=1
            if k ==3 : 
            # print("False")
                Check = 0
            # exit()
            break
    if Check == 1 :
        print("True")
        exit()

if Check == 0 :
    print("False")
                    
# ABCB
# ABCE
# SFCS
# ADEE
# .