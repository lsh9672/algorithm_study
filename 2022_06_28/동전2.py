##백준 2294번 (골드5, 디피)
import sys


n,k = map(int,sys.stdin.readline().split())

coin_list = list()

for _ in range(n):
    coin_list.append(int(sys.stdin.readline().strip()))

coin_list.sort()

dp = [0 for _ in range(k+1)]

for i in range(1,k+1):

    temp = list()

    ## 각 코인별로 i를 만들수 있는 개수를 넣고, 가장 적게 사용해야 되기 떄문에 그중에서 가장 작은값을 뽑아냄.
    for j in coin_list:
        ##코인이 만드려고 하는 i보다는 작거나 같아야되고, 이전값이 만들수 없는지(-1 로 판단)
        if i >= j and dp[j-i] != -1:
            temp.append(dp[j-i])

    ## 해당금액을 만들 수 없으면 -1
    if len(temp) == 0:
        dp[i] = -1

    else:
        dp[i] = max(temp) + 1
print(dp[k])