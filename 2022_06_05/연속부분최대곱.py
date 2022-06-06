#백준 2670번 (디피, 실버4)
import sys

n = int(sys.stdin.readline().strip())

num_list = list()

for _ in range(n):
    num_list.append(float(sys.stdin.readline().strip()))

dp = [i for i in num_list]

for i in range(1,n):

    dp[i] = max(num_list[i], num_list[i]*dp[i-1])


print("{:.3f}".format(max(dp)))


