#SWEA 4371번 (싸피,D3)
import sys


sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_19/sample_input (3).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    n = int(sys.stdin.readline().strip())

    funny_day_list = list()
    for _ in range(n):
        funny_day_list.append(int(sys.stdin.readline().strip()))

    boat_set = set()

    for i in range(1,n):
        
        temp = funny_day_list[i] - 1

        if len(boat_set) == 0:
            boat_set.add(temp)
        else:
            if temp not in boat_set:
                for j in boat_set:
                    if temp%j == 0:
                        break
                else:
                    boat_set.add(temp)

    print(f"#{test_case} {len(boat_set)}")
            

