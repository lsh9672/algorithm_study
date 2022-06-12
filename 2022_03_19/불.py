#백준  4179번(불!, 그래프 연습)
'''아이디어 1'''
#1. 불을 먼저 퍼트린다.
#2. 퍼트릴때 bfs로 퍼트리면서 각 위치마다 몇초에 퍼졌는지 기록한다.
#3. 사람이 이동할떄는 현재의 가중치(초)보다 큰 값으로 만 이동가능하다.

import sys
from collections import deque


r,c = map(int,sys.stdin.readline().split())

graph = list()

for _ in range(r):
    graph.append(list(map(str,sys.stdin.readline().strip())))

#이동정의
dx = [0,0,-1,1]
dy = [-1,1,0,0]

#불이 확산되게 함.
def fire_bfs(fire_start:list,fire_list:list)-> list:
    need_visited = deque(fire_start)

    while need_visited:

        current_x, current_y, current_count = need_visited.popleft()

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if (0 <= next_x < r) and (0 <= next_y < c) and graph[next_x][next_y] != "#":
                if fire_list[next_x][next_y] == -1:
                    fire_list[next_x][next_y] = current_count+1
                    need_visited.append([next_x,next_y,current_count+1])

def bfs(start_node:list,fire_list:list) -> int:

    need_visited = deque(list())
    need_visited.append(start_node)

    visited = [[0 for _ in range(c)] for _ in range(r)]
    
    while need_visited:
        current_x, current_y, current_count = need_visited.popleft()

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if (0 <= next_x < r) and (0 <= next_y < c):
                if visited[next_x][next_y] == 0 and graph[next_x][next_y] != "#":
                    
                    #불이 안번진 곳 - 그냥 이동하면 됨.
                    if fire_list[next_x][next_y] == -1 or current_count+1 < fire_list[next_x][next_y]:
                        need_visited.append([next_x,next_y,current_count+1])
                        visited[next_x][next_y] = 1
                    #불이 번진곳이면 몇초에 번진 곳인지 확인 - 
                    else:
                        continue

            #칸을 넘어가면, 탈출 성공
            else:
                return current_count+1

    return -1


def solution():

    fire_list = [[-1 for _ in range(c)] for _ in range(r)]
    fire_start = list()

    start_node = None
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "J":
                start_node = [i,j,0]
            
            elif graph[i][j] == "F":
                fire_list[i][j] = 0
                fire_start.append([i,j,0])

    fire_bfs(fire_start,fire_list)

    result = bfs(start_node,fire_list)

    return result

result = solution()
if result == -1:
    print("IMPOSSIBLE")
else:
    print(result)




