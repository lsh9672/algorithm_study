#SWEA 1976번 (싸피,D2)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_05/input (15).txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    result = [0,0]

    first_time,first_min, second_time,second_min = map(int,sys.stdin.readline().split())

    temp_time = (first_min+second_min)//60

    result[1] = (first_min + second_min) % 60
    
    temp_time += (first_time+second_time)

    if temp_time % 12 == 0:
        result[0] = 12
    else:
        result[0] = temp_time % 12

    print(f"#{test_case}",end=" ")
    print(*result)