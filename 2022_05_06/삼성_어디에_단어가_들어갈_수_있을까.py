#SWEA 1979번 (싸피,D2)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_06/input (16).txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0

    n, k = map(int,input().split())

    graph = list()

    for _ in range(n):
        graph.append(sys.stdin.readline().split())

    
    target = "1"*k

    ##가로
    for i in range(n):
        temp_str = "".join(graph[i])

        temp_list = temp_str.split("0")

        result += temp_list.count(target)


    ## 세로
    for i in range(n):
        temp_str = ""
        for j in range(n):
            temp_str += graph[j][i]
        
        temp_list = temp_str.split("0")

        result += temp_list.count(target)
            

                

    print(f"#{test_case} {result}")