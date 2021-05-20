x = (input())

def check(x):
    return int(x)<=255
n = len(x)
if 4<= n and n<=12:
    for i in range(1,4):
        if n - i < 3 :
            break
        if check(x[0:i]) == True:
            for j in range(i+1,i+4):
                if n - j < 2 : break
                if check(x[i:j]) == True:
                    for k in range(j+1,j+4):
                        if n - k < 1 : break
                        if check(x[j:k])== True :
                            if check(x[k:])== True:
                                result = [x[0:i],x[i:j],x[j:k],x[k:]]
                                ok = True
                                for l in result:
                                    if len(l)> 1 and result[0]=='0':
                                        ok = False
                                if ok :
                                    print(''.join((x[0:i],'.',x[i:j],'.',x[j:k],'.',x[k:])))