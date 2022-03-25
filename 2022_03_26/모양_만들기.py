#백준 16932번 (그래프 연습, 골드4)
import sys
from collections import deque

n,m  = map(int,sys.stdin.readline().split())

graph = list()

zero_list = list()

for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    graph.append(temp)
    for j in range(m):
        if temp[j] == 0:
            zero_list.append([i,j])

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(start_node:list,visited:list)-> int:

    need_visited = deque(list())
    need_visited.append(start_node)

    count = 0

    while need_visited:

        current_x,current_y = need_visited.popleft()

        count+=1

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if (0 <= next_x < n) and (0 <= next_y < m) and graph[next_x][next_y] == 1 and visited[next_x][next_y] == 0:
                visited[next_x][next_y] = 1
                need_visited.append([next_x,next_y])
    
    return count

result = list()

#0으로 되어있는 것중에 하나를 변경
for x,y in zero_list:

    graph[x][y] = 1

    visited = [[0 for _ in range(m)] for _ in range(n)]

    max_value = -1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                visited[i][j] = 1
                max_value = max(max_value,bfs([i,j],visited))

    result.append(max_value)

    #반복이 끝났으면 다음 반복을 위해 원래대로 돌려놓음
    graph[x][y] = 0
            

result.sort()
print(result[-1])
