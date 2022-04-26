#백준 2146번 (그래프, 골드3)

'''아이디어
한 섬에서 BFS탐색을 하면서, 섬들을 구분해준다.

'''

import sys
from collections import deque

n = int(sys.stdin.readline().strip())

graph = list()

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
## 상하 좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

##각 섬을 따로 표시하기 위한 탐색
def bfs(start_node:list,visited:list,count:int)-> None:

    need_visited = deque()
    need_visited.append(start_node)

    while need_visited:

        current_x, current_y = need_visited.popleft()
        
        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if (0<= next_x < n) and (0 <= next_y < n) and graph[next_x][next_y] == 1 and visited[next_x][next_y] == False:

                graph[next_x][next_y] = count
                visited[next_x][next_y] = True
                need_visited.append([next_x,next_y])

## 다리길이 계산을 위한 bfs
def bfs2(start_node:list,island_num:int, bridge_visited:list)->None:
    global min_result


    need_visited = deque(start_node)

    while need_visited:
        current_x,current_y = need_visited.popleft()

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if (0 <= next_x < n) and (0 <= next_y < n):

                ##다른섬에 도달했다면,
                if graph[next_x][next_y] != island_num and graph[next_x][next_y] < 0:
                    min_result = min(min_result,bridge_visited[current_x][current_y])
                    return
                
                if graph[next_x][next_y] == 0 and bridge_visited[next_x][next_y] == -1:
                    bridge_visited[next_x][next_y] = bridge_visited[current_x][current_y] + 1
                    need_visited.append([next_x,next_y])
    
## 상하좌우에 0이 있는지 확인
def zero_check(x,y)-> bool:

    for i in range(4):
        next_x = x+dx[i]
        next_y = y+dy[i]

        if (0 <= next_x < n) and (0 <= next_y < n):
            
            if graph[next_x][next_y] == 0:
                return True

    return False

visited = [[False for _ in range(n)] for _ in range(n)]

count = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            visited[i][j] =  True
            count -= 1
            graph[i][j] = count
            bfs([i,j],visited,count)


min_result = 1000000

for island_num in range(count,0):
    start_node = list()
    bridge_visited = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == island_num and zero_check(i,j) == True: 
                bridge_visited[i][j] = 0
                
                start_node.append([i,j])
                
    bfs2(start_node,island_num,bridge_visited)

print(min_result)

