n = int(input())
def Tao(p,left,right,a=[]):
    if right== 0:
        a.append(p)
        return a

    if left: Tao(p + '(', left-1, right)
    if right > left: Tao(p + ')', left, right-1)
    
x = Tao('', n, n)
for i in x :
    print(i)
# source code