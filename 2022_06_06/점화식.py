#백준 13699번 (디피, 실버4)
import sys


n = int(sys.stdin.readline().strip())

dp = [0 for _ in range(36)]

dp[0] = 1

for i in range(1,n+1):
    
    for j in range(0,i):
        dp[i] += dp[j]*dp[i-1-j]


print(dp[n])