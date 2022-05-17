#SWEA 3750번 (싸피, D3)

import sys

sys.setrecursionlimit = 10**6

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_17/sample_input (18).txt", "r")

def resursive(num:str):
    global temp
    if len(num) == 1:
        temp = int(num)
        return

    else:
        total = 0
        for i in num:
            total += int(i)
        
        resursive(str(total))
    return 


T = int(input())

input_dp = [sys.stdin.readline().strip() for _ in range(T)]
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    # n = sys.stdin.readline().strip()

    temp = 0
    resursive(input_dp[test_case-1])
    

    print(f"#{test_case} {temp}")

