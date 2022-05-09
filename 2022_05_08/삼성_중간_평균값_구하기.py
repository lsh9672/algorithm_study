#SWEA 1984번 (싸피,D2)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_08/input (18).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0

    num_list = list(map(int,sys.stdin.readline().split()))

    num_list.sort()

    num_list = num_list[1:-1]

    result = round(sum(num_list)/len(num_list))

    print(f"#{test_case} {result}")