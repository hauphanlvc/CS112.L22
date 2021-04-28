import io,os,sys
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
sys.stdin = open("DemTien.txt","r")
sys.stdout = open("DemTien_1.txt","w")
n = int(input())
Count = 0
Min = list()

for i in range(0,(n//500000)+1):
    for j in range(0,((n-i*500000)//200000)+1):
        for k in range(0,((n-i*500000 - j*200000) //100000)+1):
            for l in range(0,((n-i*500000 - j*200000 - k*100000))//50000+1):
                for m in range(0,((n-i*500000 - j*200000 - k*100000- l*50000)//20000)+1):
                    Tien = i*500000+j*200000+k*100000+l*50000+m*20000
                    if Tien == n :
                        Count+= 1
                        Min.append(i+j+k+l+m)
# Min = 1000000000
if Min == 1000000000:
    print("0 0")
else :
    print(Count,min(Min))