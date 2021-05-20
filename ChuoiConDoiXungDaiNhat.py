def solve(s):
    n = len(s)
    table =[[True]*n] * n
    maxLength = 1 
    i = 0
    start = 0 
    i = 0 
    for i in range(n-1):
        if s[i]==s[i+1]:
            table[i][i+1] = True
            start = i 
            maxLength = 2 
    for k in range(3,n+1):
        
        for i in range(n-k):
            j = i +k -1 
            if table[i+1][j-1] and s[i]==s[j] :
                table[i][j]= True
                if k > maxLength:
                    start = i 
                    maxLength = k 
            
    return s[start:start+maxLength]
print(solve(input()))

#https://stackoverflow.com/questions/67261887/optimal-brute-force-solution-for-finding-longest-palindromic-substring