import io,os,sys
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
sys.stdin = open("daungoac.txt","r")
sys.stdout = open("outdaungoac.txt","w")
n = int(input())

def backtrack(ans,S = [], left = 0, right = 0):
    if len(S) == 2 * n:
        ans.append("".join(S))
        return
    if left < n:    
        S.append("(")
        backtrack(ans,S, left+1, right)
        S.pop()
    if right < left:
        S.append(")")
        backtrack(ans,S, left, right+1)
        S.pop()
ans = []
backtrack(ans)
for i in ans:
    print(i)

# source code : https://leetcode.com/problems/generate-parentheses/solution/