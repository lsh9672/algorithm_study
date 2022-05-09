#SWEA 1860번 (싸피, D3)
import sys


sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_09/input (23).txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = "Possible"

    n,m,k = map(int,sys.stdin.readline().split())

    people_time = list(map(int,sys.stdin.readline().split()))

    people_time.sort()

    bread_count = 0 

    time_count = 0
    
    for i in range(n):
        
        ##x초 까지 만들어진 붕어빵의 개수
        if (((people_time[i]//m) * k) - (i+1)) < 0:
            result = "Impossible"

            break


    print(f"#{test_case} {result}")