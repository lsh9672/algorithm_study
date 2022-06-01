#백준 1912번 (디피, 실버2)
import sys


n = int(sys.stdin.readline().strip())

num_list = list(map(int,sys.stdin.readline().split()))

dp = [0 for _ in range(n)]
dp[0] = num_list[0]

for i in range(n-1):
    dp[i+1] = max(dp[i] + num_list[i+1], num_list[i+1])

print(max(dp))
