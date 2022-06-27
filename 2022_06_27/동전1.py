#백준 2293번 (디피, 골5)

'''
이 문제의 핵심은, k으로 만들어야 되는 문제를 1~k원으로 만드는 작은 문제로 쪼개서 볼 수 있어야 함.
1원짜리 동전이 있다고 가정했을때, 2원은 1원을 만들수 있는 경우에서 1원을 더하는 경우.
즉, 이렇게 1원부터 K원까지 누적해서 쌓아나가며 최종적으로 k원을 만드는 경우의 수를 구할 수 있게 됨.
'''
import sys

n,k = map(int,sys.stdin.readline().split())

num_list = list()

for _ in range(n):
    num_list.append(int(sys.stdin.readline().strip()))

num_list.sort()

dp = [0 for _ in range(k+1)]

dp[0] = 1

for i in num_list:
    for j in range(i,k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]

print(dp[k])