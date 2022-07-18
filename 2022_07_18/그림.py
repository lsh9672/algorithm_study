#백준 1926번 (실버1, 그래프)
import sys
from collections import deque


n, m = map(int,sys.stdin.readline().split())

graph = list()

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(start_node:list):

    need_visited = deque()
    need_visited.append(start_node)

    graph[start_node[0]][start_node[1]] = 0

    count = 1

    while need_visited:

        current_x, current_y = need_visited.popleft()

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if (0<=next_x < n) and (0 <= next_y < m) and graph[next_x][next_y] == 1:
                graph[next_x][next_y] = 0
                need_visited.append([next_x,next_y])
                count +=1

    return count

result = 0
max_value = -1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            result += 1
            max_value = max(max_value,bfs([i,j]))

print(result)
print(max_value)
