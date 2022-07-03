#백준 1261번 (그래프,골드4)
import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

graph = list()

for _ in range(m):

    temp = list(sys.stdin.readline().strip())
    graph.append(temp)

##상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start_node:list):
    visited = [[-1 for _ in range(n)] for _ in range(m)]

    need_visited = deque()

    need_visited.append(start_node)

    visited[start_node[0]][start_node[1]] = 0

    while need_visited:

        current_x,current_y = need_visited.popleft()

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if (0 <= next_x < m) and (0 <= next_y < n) and visited[next_x][next_y] == -1:
                if graph[next_x][next_y] == "0":
                    need_visited.appendleft([next_x,next_y])
                    visited[next_x][next_y] = visited[current_x][current_y]

                else:
                    need_visited.append([next_x,next_y])
                    visited[next_x][next_y] = visited[current_x][current_y] + 1

    return visited[m-1][n-1]

print(bfs([0,0]))