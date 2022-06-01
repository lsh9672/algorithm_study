#백준 22857번 (디피, 실버3)
import sys

n, k = map(int,sys.stdin.readline().split())

num_list = [0] + list(map(int,sys.stdin.readline().split()))

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(k+1):
        
        ##짝수
        if num_list[i] % 2 == 0:
            dp[i][j] = dp[i-1][j]+1
        ## 홀수
        if j!=0 and num_list[i] % 2 != 0:
            dp[i][j] = dp[i-1][j-1]

result = -1

for i in dp:
    result = max(result, i[k])

print(result)

