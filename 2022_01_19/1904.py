# 백준 1904 타일 (dp)

#점화식 = dp[i] = dp[i-1]+dp[i-2]
import sys


def solution(num:int) -> int:

    dp = [0] * 1000001
    dp[1] = 1
    dp[2] = 2

    for i in range(3,num+1):
        #int를 넘어가기 떄문에 저장할떄 %연산을 계속해줘야됨.
        dp[i] = (dp[i-1] + dp[i-2])%15746

    
    return dp[num]

n = int(sys.stdin.readline())

print(solution(n))
