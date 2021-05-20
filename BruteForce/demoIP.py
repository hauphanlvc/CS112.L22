import io,os,sys
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
s = input()
def Check(A,s):
    result = [(s[0:A[0]]),(s[A[0]:A[1]]),(s[A[1]:A[2]]),(s[A[2]:])]
    for i in result:
        if len(i)> 1 and i[0]=='0':
            return False
    if int(s[0:A[0]]) <= 255 and int(s[A[1]:A[2]]) <= 255 and int(s[A[0]:A[1]]) <= 255 and int(s[A[2]:]) <= 255:
        return True
    return False
def BackTracking(i,s,A):    
        if i == 3 : 
            if Check(A,s):
                result = [(s[0:A[0]]),(s[A[0]:A[1]]),(s[A[1]:A[2]]),(s[A[2]:])]
                print('.'.join(map(str,result)))            
        else:
            Si = range(A[i-1]+1,min(len(s),A[i-1]+4))
            for x in Si:
                A[i] = x 
                BackTracking(i+1,s,A)

A = [0,0,0,0]
n = len(s)
if 4<= n and n<=12:
    BackTracking(0,s,A)