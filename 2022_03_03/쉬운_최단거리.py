#백준 14940번 - 쉬운 최단거리
import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

graph = []

start_node = [0,0]

for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))

    graph.append(temp)
    if 2 in temp:
        start_node[0] = i
        start_node[1]=temp.index(2)


# 탐색한 곳은 0으로 변경
def bfs(start_node):

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]


    need_visited = deque(list())

    need_visited.append(start_node)

    while need_visited:

        current_x, current_y = need_visited.popleft()

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            if 0 <= next_x < n and 0<= next_y < m and graph[next_x][next_y] == 1:
                graph[next_x][next_y] = graph[current_x][current_y]+1
                need_visited.append([next_x,next_y])


bfs(start_node)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0,end=" ")
        else:
            print(graph[i][j]-2,end=" ")
    
    print("")


