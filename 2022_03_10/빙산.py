#백준 2573 빙산

import sys
from collections import deque


n,m = map(int,sys.stdin.readline().split())

graph = []

dx = [0,0,-1,1]
dy = [-1,1,0,0]

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

def bfs(start_node:list) -> list:

    
    need_visited = deque(list())
    need_visited.append(start_node)
    visited[start_node[0]][start_node[1]] = 1

    while need_visited:

        current_x,current_y = need_visited.popleft()

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if next_x >=0 and next_x < n and next_y >= 0 and next_y < m:

                if graph[next_x][next_y] != 0 and visited[next_x][next_y] == 0:
                    visited[next_x][next_y] = 1
                    need_visited.append([next_x,next_y])
                
                elif graph[next_x][next_y] == 0:
                    count_ice[current_x][current_y] += 1

result = 0

time = 0
    
while True:

    #0이면 방문하지 않은 곳, 1이면 방문한 곳
    visited = [[0 for _ in range(m)] for _ in range(n)]

    #빙하를 얼마나 깍야야 되는지
    count_ice = [[0 for _ in range(m)] for _ in range(n)]

    #탐색하면서 연결요소가 2개 이상인지
    link_count = 0

    for x in range(n):
        for y in range(m):
            if graph[x][y] != 0 and visited[x][y] == 0:
                bfs([x,y])
                link_count += 1

    if link_count >= 2:
        result = time
        break

    #한번녹이면 시간 +1
    time += 1

    #빙하 하나씩 줄이기 - 한번에 없애야됨
    check = True
    for i in range(n):
        for j in range(m):
            if count_ice[i][j] != 0:
                graph[i][j] -= count_ice[i][j]
                check = False

                if graph[i][j] < 0:
                    graph[i][j] = 0

    if check == True:
        break

print(result)
