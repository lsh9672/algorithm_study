##SWEA 1948번 (싸피, D2)

import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_02/input (9).txt", "r")

T = int(input())

day_list = [0,31,28,31,30,31,30,31,31,30,31,30,31]
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    first_month,first_day, second_month,second_day = list(map(int,sys.stdin.readline().split()))

    result = 0

    first_total_day = first_day
    second_total_day = second_day

    for i in range(0,first_month):
        first_total_day += day_list[i]
    
    for i in range(0,second_month):
        second_total_day += day_list[i]

    
    result = second_total_day - first_total_day + 1

    print(f"#{test_case} {result}")

    