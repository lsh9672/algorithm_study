import sys
from collections import deque


#세로,가로
n,m = map(int,sys.stdin.readline().split())


graph = []

for _ in range(n):
    graph.append(list(sys.stdin.readline().strip()))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(start_node):

    visited = [[0 for _ in range(m)] for _ in range(n)]
    
    need_visited = deque(list())

    need_visited.append(start_node)

    visited[start_node[0]][start_node[1]] = 1

    count = 0
    while need_visited:
        current_x, current_y = need_visited.popleft()
        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if (0<= next_x < n ) and (0 <= next_y < m) and graph[next_x][next_y] == "L" and visited[next_x][next_y] == 0:
                visited[next_x][next_y] = visited[current_x][current_y] + 1
                need_visited.append([next_x,next_y])
                #bfs탐색에서 나올수 있는 최대 값을 누적시켜둠
                count = max(count,visited[next_x][next_y])

    return count


result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "L":
            #지나간 곳을 업데이트 하지않음, 육지의 시작점에 따라서 거리가 달라지기 때문에.
            result = max(result,bfs([i,j]))

#시작을 0이 아닌 1로 시작했기 때문에 -1을 해줘야됨(0을 탐색안한곳으로 하기 위해서 시작점을 1로 함.)
print(result-1)