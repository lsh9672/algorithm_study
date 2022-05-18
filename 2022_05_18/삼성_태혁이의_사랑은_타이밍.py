#SWEA 4299번 (싸피,D3)

import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_18/sample_input (2).txt", "r")

T = int(input())

total_minute = 11*24*60 + 11*60+11

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    day,hour,minute = map(int,sys.stdin.readline().split())

    temp_minute = day * 24 * 60 + hour*60 + minute

    result = 0

    if temp_minute < total_minute:
        result = -1

    else:
        result = temp_minute - total_minute

    print(f"#{test_case} {result}")