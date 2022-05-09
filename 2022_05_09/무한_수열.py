#백준 1351번(자료구조,골드5)
import sys

n,p,q = map(int,sys.stdin.readline().split())

dp = dict()

def dfs(n):

    if n in dp:
        return dp[n]

    dp[n] = dfs(n//p) + dfs(n//q)

    return dp[n]

dp[0] = 1

print(dfs(n))
