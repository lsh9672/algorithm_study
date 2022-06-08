#백준 11048 (디피, 실버2)
import sys

n,m = map(int,sys.stdin.readline().split())

graph = [[0 for _ in range(m+1)]]

for _ in range(n):
    graph.append([0]+list(map(int,sys.stdin.readline().split())))

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = graph[i][j] + max(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])

print(dp[n][m])