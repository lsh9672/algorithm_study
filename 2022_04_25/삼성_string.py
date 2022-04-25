#SWEA 1213번 (싸피 연습,D3)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_04_25/test_input.txt", "r")


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for _ in range(10):
    test_case = int(input())

    pattern = input().strip()

    input_string = input().strip()

    print(f"#{test_case} {input_string.count(pattern)}")


