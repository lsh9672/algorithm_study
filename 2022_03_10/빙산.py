#백준 5639번 (이진 검색 트리)
import sys
from collections import deque


n,m = map(int,sys.stdin.readline().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

def bfs(start_node):

    visited = [[0 for _ in range(m)] for _ in range(n)]

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    need_visited = deque(list())
    need_visited.append(start_node)

    while need_visited:

        current_x,current_y = need_visited.popleft()

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if next_x >=0 and next_x < n and next_y >= 0 and next_y < m :

                if graph[next_x][next_y] != 0:
                    if visited[next_x][next_y] != 1:
                        need_visited.append([next_x,next_y])
                        visited[next_x][next_y] = 1
                
                else:
                    graph[current_x][current_y] -= 1

                    if graph[current_x][current_y] < 0:
                        graph[current_x][current_y] = 0

bfs([1,1])
print(*graph)
                    

