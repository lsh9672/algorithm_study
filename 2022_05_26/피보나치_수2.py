# 백준 2748번 (dp,브론즈1)
import sys


n = int(sys.stdin.readline().strip())

dp = [0 for _ in range(91)]
dp[1] = 1
dp[2] = 1

for i in range(3,n+1):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[n])

