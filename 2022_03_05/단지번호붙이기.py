#백준 2667번(실버1, 그래프)
import sys
from collections import deque


n = int(sys.stdin.readline())

#지도
graph = list()

#지도 채우기
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip())))

#bfs함수 정의
def bfs(start_node:list)-> int:

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    #집 개수 세기
    count = 0

    need_visited = deque(list())

    need_visited.append(start_node)

    graph[start_node[0]][start_node[1]] = 0

    while need_visited:
        current_x,current_y = need_visited.popleft()

        count += 1

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if next_x >= 0 and next_x < n and next_y >= 0 and next_y < n and graph[next_x][next_y] == 1:
                graph[next_x][next_y] = 0
                need_visited.append([next_x,next_y])

    return count


#총 단지 개수
total_count = 0

#각 단지내 집개수 
home_count_list = list()

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home_count_list.append(bfs([i,j]))
            total_count += 1

print(total_count)

for i in home_count_list:
    print(i)

