#백준 1106번 (골드5)

import sys

c,n = map(int, sys.stdin.readline().split())

num_list = list()

for _ in range(n):
    ## 홍보비용, 고객수
    num_list.append(list(map(int,sys.stdin.readline().split())))


##각 고객수 별 비용
dp = [1e8 for _ in range(c+100)]
dp[0] = 0

## 홍보비용, 고객수
for a,b in num_list:
    for i in range(b,c+100):
        dp[i] = min(dp[i], dp[i-b] + a)


print(min(dp[c:]))



