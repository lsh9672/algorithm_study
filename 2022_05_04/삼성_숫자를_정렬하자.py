#SWEA 1966번 (싸피, D2)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_04/input (12).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input().strip())

    num_list = list(map(int,input().split()))

    num_list.sort()

    print(f"#{test_case}", end=" ")
    print(*num_list)