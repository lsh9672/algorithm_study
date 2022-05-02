#SWEA 1945번 (싸피, D2)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_02/input (4).txt", "r")


T = int(input())

num_list = [2,3,5,7,11]
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    target_num = int(sys.stdin.readline().strip())

    result_list = [0] * 5

    for i in range(len(num_list)):

        while target_num%num_list[i] == 0:
            result_list[i] += 1
            target_num //= num_list[i]

    print(f"#{test_case}", end = " ")
    print(*result_list)