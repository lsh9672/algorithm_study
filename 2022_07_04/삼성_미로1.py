#SWEA 1226번 (D4, 사전과제)
import sys
from collections import deque

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_07_04/input (2).txt", "r")


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start_node:list,graph:list)->int:

    need_visited = deque()
    need_visited.append(start_node)

    graph[start_node[0]][start_node[1]] = 1


    while need_visited:
        current_x,current_y = need_visited.popleft()

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if (0 <= next_x < 16) and (0 <= next_y < 16) and graph[next_x][next_y] != 1:

                if graph[next_x][next_y] == 3:
                    return 1
                else:
                    need_visited.append([next_x,next_y])
                    graph[next_x][next_y] = 1

    return 0
# T = int(input())
T=10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for _ in range(1, T + 1):

    test_case = int(input().strip())
    result = 0
    graph = list()

    for _ in range(16):
        temp = list(map(int,list(input().strip())))

        graph.append(temp)
    
    start_node = None

    for i in range(16):
        check = True
        for j in range(16):
            if graph[i][j] == 2:
                result = bfs([i,j],graph)
                check = False
                break
        if check == False:
            break


    print(f"#{test_case} {result}")