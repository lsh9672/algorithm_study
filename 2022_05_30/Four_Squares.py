#백준 17626번 (실버4, 디피)
import sys
import math


n = int(sys.stdin.readline())

dp = [0 for _ in range(n+1)]

dp[1] = 1

for i in range(2,n+1):
    min_value = 1e9
    count = 1

    while count**2 <= i:
        min_value = min(min_value,dp[i-(count**2)])

        count += 1

    dp[i] = min_value + 1

print(dp[n])

