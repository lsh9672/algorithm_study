#SWEA 1983번 (싸피, D2)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_08/input (17).txt", "r")

hakjum_list = ["A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,k = map(int,sys.stdin.readline().split())

    score_list = list()

    for _ in range(n):
        middle,final,hw = map(int,sys.stdin.readline().split())

        temp = (middle*0.35)+ (final * 0.45) + (hw * 0.2)

        score_list.append(temp)

    
    target_score = score_list[k-1]

    score_list.sort(reverse=True)

    temp_value = n//10
    # print(temp_value)

    index = 1

    result_index = 0

    while True:
        if score_list[(temp_value*index)-1] <= target_score:
            result_index = index
            break
        
        index += 1

    print(f"#{test_case} {hakjum_list[result_index-1]}")
