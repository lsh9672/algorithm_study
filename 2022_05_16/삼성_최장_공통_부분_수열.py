#SWEA 3304번 (싸피, D3) - LCS

import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_16/sample_input (8).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    first_str,second_str = sys.stdin.readline().strip().split()

    result= 0

    dp = [[0 for _ in range(len(second_str)+1)] for _ in range(len(first_str)+1)]

    for i in range(1,len(first_str)+1):
        for j in range(1,len(second_str)+1):
            if first_str[i-1] == second_str[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1

            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    result = dp[len(first_str)][len(second_str)]


    print(f"#{test_case} {result}")
    
