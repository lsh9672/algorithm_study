#백준 11727번 (디피, 실버3)
import sys


n = int(sys.stdin.readline().strip())

dp = [0 for _ in range(1001)]

dp[1] = 1
dp[2] = 3

for i in range(3,n+1):
    dp[i] = dp[i-2]*2 + dp[i-1]

print(dp[n]%10007)