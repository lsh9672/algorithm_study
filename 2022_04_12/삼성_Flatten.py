# SWEA 1208번(싸피대비, D3)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_04_12/input.txt","r")


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):

    dump_count = int(input())

    num_list = list(map(int,input().split()))

    for _ in range(dump_count):
        num_list[num_list.index(max(num_list))] -= 1
        num_list[num_list.index(min(num_list))] += 1

    print(f"#{test_case} {max(num_list) - min(num_list)}")
