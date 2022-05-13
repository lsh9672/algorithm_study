#SWEA 3142번(싸피, D3)

import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_13/sample_input (5).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = [0,0]

    n,m = map(int,sys.stdin.readline().split())

    result[0] = 2 * m - n
    result[1] = n - m


    print(f"#{test_case}", end = " ")
    print(*result)