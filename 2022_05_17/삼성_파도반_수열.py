# SWEA 3376번 (싸피,D3)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_17/sample_input (13).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n = int(sys.stdin.readline().strip())

    dp = [0] * (101)
    dp[1] = 1
    dp[2] = 1

    for i in range(3,n+1):
        dp[i] = dp[i-2] + dp[i-3]

    print(f"#{test_case} {dp[n]}")