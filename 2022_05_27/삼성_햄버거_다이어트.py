#SWEA 5215번 (싸피,d3)
import sys
from itertools import combinations

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_27/sample_input (12).txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    n,l = map(int,sys.stdin.readline().split())

    num_list = list()

    result = 0

    for _ in range(n):
        num_list.append(list(map(int,sys.stdin.readline().split())))

    for i in range(1,n+1):
        temp_list = combinations(num_list,i)

        for j in temp_list:
            total_kal = 0
            total_score = 0
            for score, kal in j:
                total_kal += kal
                total_score += score
            
            if total_kal <= l:
                result = max(result,total_score)

    print(f"#{test_case} {result}")