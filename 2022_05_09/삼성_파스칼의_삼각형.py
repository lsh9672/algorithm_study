#SWEA 2005번 (싸피,D2)

import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_09/input (22).txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(sys.stdin.readline().strip())

    graph= [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        graph[i][0] = 1

    for i in range(1,n):
        for j in range(1,i+1):
            graph[i][j] = graph[i-1][j-1] + graph[i-1][j]


    print(f"#{test_case}")
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                
                print(graph[i][j], end = " ")
        
        print("")
    