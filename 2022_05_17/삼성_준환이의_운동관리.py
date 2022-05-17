# SWEA 3431 (싸피,D3)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_17/sample_input (11).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    l,u,x = map(int,sys.stdin.readline().split())

    result = 0

    if x < l:
        result = l-x
    elif x > u:
        result = -1

    print(f"#{test_case} {result}")