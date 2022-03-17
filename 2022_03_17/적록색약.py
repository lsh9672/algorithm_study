#백준 10026번 (그래프 탐색, 골드5)
from re import A
import sys
from collections import deque


n = int(sys.stdin.readline())

graph = []

color_list = ["R","G","B"]

color_list_2 = ["R","B"]

for _ in range(n):

    graph.append(list(sys.stdin.readline().strip()))

#상하좌우 이동 정의
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(start_node:list,color:str,color_blindness:bool,visited:list)-> int:
    
    need_visited = deque(list())
    need_visited.append(start_node)

    while need_visited:

        current_x,current_y = need_visited.popleft()

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if (0 <= next_x < n) and (0 <= next_y < n) and visited[next_x][next_y] == 0:
                
                #일반인일때
                if color_blindness == False:
                    if graph[next_x][next_y] == color:
                        visited[next_x][next_y] = 1
                        need_visited.append([next_x,next_y])
                    
                    

                #색맹일때랑
                else:
                    #빨간색이 입력으로 들어올때랑, 파란색이 들어올때 두가지로 나눠야됨.
                    if color == "B":
                        if graph[next_x][next_y] == color:
                            visited[next_x][next_y] = 1
                            need_visited.append([next_x,next_y])

                    else:
                        if graph[next_x][next_y] != "B":
                            visited[next_x][next_y] = 1
                            need_visited.append([next_x,next_y])


    return 1

    

normal_result = 0
blindness_result = 0

#일반인 color_blindness: false
for color in color_list:

    visited = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == color and visited[i][j] == 0:
                visited[i][j] = 1
                normal_result += bfs([i,j],color,False,visited)

#색맹 color_blindness:True
for color in color_list_2:

    visited = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if color == "R":
                if (graph[i][j] == "R" or graph[i][j] == "G") and visited[i][j] == 0:
                    visited[i][j] = 1
                    blindness_result += bfs([i,j],color,True,visited)
            else: 
                if graph[i][j] == color and visited[i][j] == 0:
                    visited[i][j] = 1
                    blindness_result += bfs([i,j],color,True,visited)

print(normal_result,blindness_result)

