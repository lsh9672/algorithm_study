#백준 2579번(dp,실버3)
import sys

n = int(sys.stdin.readline())

input_height = [0 for _ in range(301)]

dp = [0 for _ in range(301)]

for i in range(1,n+1):
    input_height[i] = int(sys.stdin.readline())

dp[1] = input_height[1]
dp[2] = input_height[1]+input_height[2]
dp[3] = max(input_height[1]+input_height[3],input_height[2]+input_height[3])

for i in range(4,n+1):
    dp[i] = max(dp[i-2]+input_height[i], dp[i-3]+input_height[i-1]+input_height[i])

print(dp[n])
