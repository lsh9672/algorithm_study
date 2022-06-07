#백준 14501번 (디피,실버3)
import sys

n = int(sys.stdin.readline().strip())

chart = []

for _ in range(n):
    chart.append(list(map(int,sys.stdin.readline().split())))

## dp에는 받을수 있는 수익을 넣음
dp = [0 for _ in range(16)]

for i in range(n-1,-1,-1):

    ## 해당일에서 상담에 걸리는 시간을 더했을떄, 회사에 있는 날(n)보다 크면 상담 불가
    if i + chart[i][0] > n:

        ##해당 날짜의 상담 시간이 퇴사일이후라 받을수 없으면 그 다음날 값을 가져옴
        ##i날에 못받으면 i+1날의 수익을 가져옴(0일수도, 값이 있을수도 있음)
        dp[i] = dp[i+1]

    else:

        ##상담을 하는 것과 안하는 것중에 큰 값을 저장함
        ## 상담을 안한다면 그 다음날의 값을 가져옴, 상담을 한다면, 해당 날짜와, 해당 날짜에서 상담을 하고 나서 가능한 날의 보수를 가져옴
        dp[i] = max(dp[i+1], dp[i+chart[i][0]] + chart[i][1])

print(dp[0])