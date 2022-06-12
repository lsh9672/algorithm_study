#SWEA 1289번(싸피, D3)

import sys


# sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_01/input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    result = 0

    temp = sys.stdin.readline().strip()

    current_bit = "0"

    for i in temp:

        if current_bit == i:
            continue

        else:
            result += 1
            current_bit = i


    print(f"#{test_case} {result}")
    