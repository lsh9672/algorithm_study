#백준 2638 (그래프 연습, 골드 4)
import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

graph = []

for _ in range(n):

    graph.append(list(map(int,sys.stdin.readline().split())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs():

    visited = [[0 for _ in range(m)] for _ in range(n)]

    next_remove_cheese = list()

    need_visited = deque(list())

    need_visited.append([0,0])
    
    visited[0][0] = 1

    while need_visited:

        current_x, current_y = need_visited.popleft()


        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if (0 <= next_x < n) and (0 <= next_y < m):
                
                if visited[next_x][next_y] == 0:
                # print(next_x,next_y)

                    #공기 일때,
                    if graph[next_x][next_y] == 0:
                        need_visited.append([next_x,next_y])
                        visited[next_x][next_y] = 1

                    else:
                        visited[next_x][next_y] += 1

                
                #치즈 일때
                elif visited[next_x][next_y] == 1:

                    if graph[next_x][next_y] == 1:
                        visited[next_x][next_y] += 1
                        next_remove_cheese.append([next_x,next_y])

                
                else:
                    continue


    return next_remove_cheese


time_count = 0

while True:

    #녹일 치즈 위치를 가져옴
    cheese_location = bfs()
    # print(cheese_location)

    if len(cheese_location) == 0:
        break
    
    #치즈를 녹임
    for x,y in cheese_location:
        graph[x][y] = 0

    time_count+=1

print(time_count)