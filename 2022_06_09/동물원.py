# 백준 1309 (디피, 실버1)
import sys

'''
2차원배열을 만들때, 각 컬럼을 0일떄는 맨위의 두칸의 우리가 둘다 비어있을떄, 1이면 왼쪽에만 있을떄, 2이면 오른쪽에만 있을때
'''

n = int(sys.stdin.readline().strip())

dp = [[0,0,0] for _ in range(100001)]

## n==1 일떄는 전부 1개씩 존재

for i in range(3):
    dp[1][i] = 1

for i in range(2,n+1):

    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901

print(sum(dp[n])%9901)
