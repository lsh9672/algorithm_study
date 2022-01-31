#백준 1149 RGB거리(dp)
import sys


'''입력'''
#집의 수
n = int(sys.stdin.readline())

dp = []

#색칠 비용 입력 - RGB
for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))

    dp.append(temp)


for i in range(1,n):
    
    #R값이면 인접한 집과는 색깔이 겹치면 안되기 때문에 바로 이전집(이전 인덱스)의 G,B중에서 작은 값을 더해줌
    dp[i][0] += min(dp[i-1][1],dp[i-1][2])
    #G값이면 인접한 집과는 색깔이 겹치면 안되기 때문에 바로 이전집(이전 인덱스)의 R,B중에서 작은 값을 더해줌
    dp[i][1] += min(dp[i-1][0],dp[i-1][2])
    #B값이면 인접한 집과는 색깔이 겹치면 안되기 때문에 바로 이전집(이전 인덱스)의 R,G중에서 작은 값을 더해줌
    dp[i][2] += min(dp[i-1][0],dp[i-1][1])

#가장 마지막 행에 조건에 맞는 최소값들이 더해져서 저장됨
#이중에서 가장 작은 값을 뽑아내면 됨
print(min(dp[-1]))

