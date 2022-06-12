#백준 11057번 (디피, 실버1)
import sys

n = int(sys.stdin.readline().strip())


dp = [1 for _ in range(10)]

for _ in range(n-1):
    for j in range(1,10):
        dp[j] += dp[j-1]

print(sum(dp) % 10007)