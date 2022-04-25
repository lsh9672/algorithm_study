## SWEA - 1209번 

import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_04_24/input.txt", "r")



# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for _ in range(10):
    test_case = int(input())

    graph = list()

    for _ in range(100):
        graph.append(list(map(int,sys.stdin.readline().split())))

    result_max = 0

    ## 각 행의 합
    for i in graph:
        
        result_max = max(result_max,sum(i))

    ## 각 열의 합
    for i in range(100):
        temp_total = 0
        for j in range(100):
            temp_total += graph[j][i]

        result_max = max(result_max, temp_total)

    ## 대각선
    right_down = 0
    left_down = 0
    for i in range(100):
        right_down += graph[i][i]
        left_down += graph[i][99-i]

    
    result_max = max(result_max,right_down)
    result_max = max(result_max,left_down)

    print(f"#{test_case} {result_max}")

