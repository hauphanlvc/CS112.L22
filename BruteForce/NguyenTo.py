import io,os,sys
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# from sympy import *
from math import sqrt
sys.stdin = open("NguyenTo.txt","r")
sys.stdout = open("NguyenTo_1.txt","w")

n = int(input())
isprime = [True for i in range(n+1)]
isprime[0]= False
isprime[1]= False
i = 2 
while i*i <= n :
    if isprime[i] == True :
        j = i*i
        while j <= n :
            isprime[j] = False
            j+=i
    i+=1
Count = 0
for i in range(2,n//2+1):
    if isprime[i] == True and isprime[n-i]== True: Count+=1
print(Count)

# Source Code : https://vnoi.info/wiki/translate/he/Number-Theory-2