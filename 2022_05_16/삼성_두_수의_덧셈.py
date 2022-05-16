##SWEA 3260번 (싸피,d3)

import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_16/sample_input (7).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0

    a,b = map(int,sys.stdin.readline().split())
    result = a+b

    print(f"#{test_case} {result}")