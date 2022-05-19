#SWEA 4466번 (싸피,D3)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_19/sample_input (4).txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0

    n,k = map(int,sys.stdin.readline().split())

    num_list = list(map(int,sys.stdin.readline().split()))

    num_list.sort(reverse=True)

    for i in range(k):
        result += num_list[i]

    print(f"#{test_case} {result}")