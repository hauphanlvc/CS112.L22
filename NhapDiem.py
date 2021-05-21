import io,os,sys
from decimal import Decimal
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
sys.stdin = open("Inputnhapdiem.txt","r")
sys.stdout = open("Outputnhapdiem.txt","w")
n = int(input())
HeSo = []
for i in range(n):
    x = int(input())
    HeSo.append(x)
Diem = float(input())
Diem*=10000

GiaTriNhoNhat = int(Diem/n)
res = []

def check(S,Diem,HeSo):
    ok = 0 
    for i in range(n):
        ok += S[i]*HeSo[i]
    
    # print(abs(ok- Diem))
    if Diem > ok and Diem - ok <= 500 :
        return True
    elif Diem < ok and ok - Diem <= 490 :
        return True
    elif Diem== ok :
        return True
    return False
def Print(S):
    for i in S:
        if abs(i - int((i/100))* 100) ==0 :
            print(int(i/100),end=' ')
        else :
            print((i/100),end=' ')
        
def BackTrack(i,S,n,Diem,HeSo):
    if i == n :
        if check(S,Diem,HeSo):
            Print(S)
            print()
            return 
            # ok = 0 
            # for i in range(len(S)):
            #     ok += S[i]*HeSo[i]
            # print("ok = ",ok)
            # print("Diem = ",Diem)
            # print(abs(ok - Diem))
            # print("-------")

    else :
        for x in range(1,41):
             
            
            d = x*25*HeSo[i]
            for j in range(i):
                d+= S[j]*HeSo[j]
            if d - Diem > 600 : return
            conlai = 0 
            for j in range(i+1,n):
                conlai+=1000*HeSo[j]
            if Diem - d - conlai > 500:
                pass
            else :
                S.append(x*25)
                BackTrack(i+1,S,n,Diem,HeSo)
                S.pop()

BackTrack(0,[],n,Diem,HeSo)