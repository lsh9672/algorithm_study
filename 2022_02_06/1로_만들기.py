#백준 1463 1로 만들기
#dp문제

import sys


n = int(sys.stdin.readline())

#여기에는 계산한 횟수를 더하는것이다

dp = [0]* (n+1)

for i in range(2,n+1):
    dp[i] = dp[i-1] + 1

    if i%2 == 0:
        # -1한경우랑 //2 한 경우 둘중에 작은 것으로 업데이트
        dp[i] = min(dp[i],dp[i//2]+1)

    if i%3 == 0:
        # -1한경우랑 //3 한 경우 둘중에 작은 것으로 업데이트
        dp[i] = min(dp[i],dp[i//3]+1)

sys.stdout.write(str(dp[n]))
