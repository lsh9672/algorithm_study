#SWEA 2948번 (싸피, D3)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_10/sample_input.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m = map(int,sys.stdin.readline().split())

    first_set = set(sys.stdin.readline().split())

    second_set = set(sys.stdin.readline().split())

    result = first_set & second_set
    

    print(f"#{test_case} {len(result)}")