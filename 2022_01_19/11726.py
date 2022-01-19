#백준 11726 2*N 타일링(dp)
import sys


def solution(num):
    dp = [0] * 10001

    dp[1],dp[2] = 1,2

    for i in range(3,num+1):
        #숫자가 너무 커져서 메모리초과가 날수도 있기 떄문에 계산할떄 마다 %10007을 해준다.
        dp[i] = (dp[i-1] + dp [i-2])%10007
    
    return dp[num]

n = int(sys.stdin.readline())
print(solution(n))
