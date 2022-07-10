#백준 1520번 (디피,골드3)
import sys
from collections import deque

m,n = map(int,sys.stdin.readline().split())

graph = list()

for _ in range(m):
    graph.append(list(map(int,sys.stdin.readline().split())))

visited = [[-1 for _ in range(n)] for _ in range(m)]

## 상, 하, 좌, 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(start_node:list):

    if start_node[0] == m-1 and start_node[1] == n-1:
        return 1

    if visited[start_node[0]][start_node[1]] != -1:
        return visited[start_node[0]][start_node[1]]

    visited[start_node[0]][start_node[1]] = 0
    for i in range(4):
        next_x = start_node[0] + dx[i]
        next_y = start_node[1] + dy[i]

        if (0 <= next_x < m) and (0 <= next_y < n):
            if graph[start_node[0]][start_node[1]] > graph[next_x][next_y]:
                visited[start_node[0]][start_node[1]] += dfs([next_x,next_y])

    return visited[start_node[0]][start_node[1]]


print(dfs([0,0]))