#백준 9461 - 파도반 수열(dp)
import sys


def solution(num):
    dp = [0]*101
    dp[1],dp[2],dp[3] = 1,1,1

    for i in range(4,num+1):
        dp[i] = dp[i-2] + dp[i-3]

    return dp[num]

n = int(sys.stdin.readline())

temp = list()

for _ in range(n):
    temp_value = int(sys.stdin.readline())
    temp.append(temp_value)

for i in temp:
    print(solution(i))