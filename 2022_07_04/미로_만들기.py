#백준 2665번 (골드4, 그래프)
import sys
import heapq

n = int(sys.stdin.readline().strip())

graph = list()

for _ in range(n):
    graph.append(sys.stdin.readline().strip())

## 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start_node:list,graph:list,n:int):
    visited = [[-1 for _ in range(n)] for _ in range(n)]

    need_visited = list()
    heapq.heappush(need_visited, [0] + start_node)

    visited[start_node[0]][start_node[1]] = 0

    while need_visited:

        current_count, current_x, current_y = heapq.heappop(need_visited)

        if visited[current_x][current_y] < current_count:
            continue
        
        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if (0 <= next_x < n) and (0 <= next_y < n):
                temp = 0
                if graph[next_x][next_y]== "0":
                    temp = 1
                else:
                    temp = 0

                if visited[next_x][next_y] == -1:
                    visited[next_x][next_y] = current_count + temp
                    heapq.heappush(need_visited, [visited[next_x][next_y],next_x,next_y])

                elif visited[next_x][next_y] > current_count + temp:
                    visited[next_x][next_y] = current_count + temp
                    heapq.heappush(need_visited,[visited[next_x][next_y],next_x,next_y])


    return visited[n-1][n-1]

print(bfs([0,0],graph,n))