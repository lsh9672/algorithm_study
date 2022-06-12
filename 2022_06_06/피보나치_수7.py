#백준 15624번 (디피, 실버4)
import sys

n = int(sys.stdin.readline().strip())

dp = [0 for _ in range(1000001)]

dp[0] = 0
dp[1] = 1

for i in range(2,n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
print(dp[n])