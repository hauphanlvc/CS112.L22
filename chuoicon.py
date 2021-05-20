s = input()
def dfs( s, path , res ):
    if not s :
        res.append(path[:])
        return 
    for i in range(1,len(s)+1):
        if s[:i] == s[i-1::-1]:
            path.append(s[:i])
            dfs(s[i:], path, res)
            path.pop()
res = []
dfs(s, [], res)
for i in res:
    print(*i)
# source code :https://leetcode.com/problems/palindrome-partitioning/discuss/41973/Python-recursiveiterative-backtracking-solution