# 백준 2206번 (벽부수고 이동하기, 골드4, 그래프)
'''아이디어'''
#1. 이전에 탐색하는 그래프들과 비슷한데 벽을 부순다는 것이 다르다.
#2. 벽은 한번만 부술수 있기 때문에, 방문 처리리스트를 3차원으로 만들어서 벽을 부셨을때와, 부시지 않았을 때로 나눠서 구한다.


import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip())))

print(graph)

def bfs():

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    visited = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]

    need_visited = deque(list())

    #x,y좌표, 벽 부순 유무
    need_visited.append([0,0,0])
    
    visited[0][0][0] = 1

    while need_visited:

        current_x,current_y,wall = need_visited.popleft()

        if current_x == n-1 and current_y == m-1:
            return visited[current_x][current_y][wall]

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            #좌표 평면 안넘어가는 확인 + 방문했는지 확인
            if next_x >= 0 and next_x < n and next_y >= 0 and next_y < m and visited[next_x][next_y][wall] == 0:

                #벽이 아니면 이동,
                if graph[next_x][next_y] == 0:
                    need_visited.append([next_x,next_y,wall])
                    visited[next_x][next_y][wall]  = visited[current_x][current_y][wall] + 1

                #벽인데, 현재 벽을 안부셔서 벽을 부술수 있다면, 벽을 부수고 이동
                if graph[next_x][next_y] == 1 and wall == 0:
                    need_visited.append([next_x,next_y,1])
                    visited[next_x][next_y][1] = visited[current_x][current_y][wall] + 1

    return -1

print(bfs())



