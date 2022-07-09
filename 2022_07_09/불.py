#백준 5427(불,골드4)
import sys
from collections import deque

n = int(sys.stdin.readline().strip())

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def fire_bfs(start_node:list,visited:list,graph:list):

    need_visited = deque(start_node)


    while need_visited:

        current_x,current_y, current_count = need_visited.popleft()
        # print(current_x,current_y)

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            # print(next_x,next_y)

            if (0 <= next_x < h) and (0 <= next_y < w) and visited[next_x][next_y] == -1 and (graph[next_x][next_y] == "." or graph[next_x][next_y] == "@"):
                # print(next_x,next_y)
                visited[next_x][next_y] = current_count + 1
                need_visited.append([next_x,next_y,visited[next_x][next_y]])

        
def people_bfs(start_node:list,visited:list,graph:list,fire_field:list):

    need_visited = deque()
    need_visited.append(start_node)

    visited[start_node[0]][start_node[1]] = 0


    while need_visited:

        current_x, current_y, current_count = need_visited.popleft()

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if (0 <= next_x < h) and (0 <= next_y < w):
                if visited[next_x][next_y] == -1 and graph[next_x][next_y] == "." and (fire_field[next_x][next_y] == -1 or fire_field[next_x][next_y] > current_count + 1):
                    visited[next_x][next_y] = current_count + 1
                    need_visited.append([next_x,next_y,current_count+1])

            else:
                return current_count+1

    return -1

            

for _ in range(n):
    w,h = map(int,sys.stdin.readline().split())

    graph = list()

    for _ in range(h):
        graph.append(sys.stdin.readline().strip())

    result = 0

    fire_start_node = list()

    people_start_node = None

    fire_field = [[-1 for _ in range(w)] for _ in range(h)]
    people_field = [[-1 for _ in range(w)] for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == "*":
                fire_field[i][j] = 0
                fire_start_node.append([i,j,0])

            elif graph[i][j] == "@":
                people_start_node = [i,j,0]

    

    fire_bfs(fire_start_node,fire_field,graph)

    result = people_bfs(people_start_node,people_field,graph,fire_field)

    if result == -1:
        print("IMPOSSIBLE")

    else:
        print(result)
