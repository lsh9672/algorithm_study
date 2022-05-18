#백준 3809번 (싸피, D3)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_18/sample_input (19).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input().strip())
    result = 0

    total_str = ""

    while True:

        if len(total_str) == n:
            break

        total_str += "".join(input().strip().split())
    

    value = 0
    while True:

        if str(value) not in total_str:
            result = value
            break

        value += 1

    print(f"#{test_case} {result}")