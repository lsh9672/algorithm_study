#백준 17141번 (골드4, 그래프)

import sys
from itertools import combinations
from collections import deque


n,m = map(int,sys.stdin.readline().split())


graph = list()

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

##방향 - 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start_node:list,visited:list,test_graph:list):

    need_visited = deque(start_node)

    max_time = 3

    while need_visited:

        current_x,current_y = need_visited.popleft()

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if (0 <= next_x < n) and (0 <= next_y < n) and visited[next_x][next_y] == 0 and test_graph[next_x][next_y] != 1:
                max_time = max(max_time, test_graph[current_x][current_y]+1)

                test_graph[next_x][next_y] = test_graph[current_x][current_y]+1

                need_visited.append([next_x,next_y])

                visited[next_x][next_y] = 1
    
    return max_time

    
## 원본그래프는 두고, 복사해서 새로 만드는 함수
def copy_graph()-> list:
    temp = list()

    for i in graph:
        temp.append(i[:])

    return temp

## 바이러스를 퍼트렸을떄, 2또는 0이 있는지 확인
def check_graph(test_graph:list)-> bool:
    for i in range(n):
        for j in range(n):
            if test_graph[i][j] == 2 or test_graph[i][j] == 0:
                return False
    
    return True
##바이러스를 놓을수 있는 위치를 저장함.
virus_loc = list()

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus_loc.append([i,j])

##최소시간  - 출력할 결과
min_time = 3000

## 조합으로 놓을수 있는 모든 경우를 뽑음            
for temp_loc in combinations(virus_loc,m):
    test_graph = copy_graph()

    start_node = list(temp_loc)

    visited = [[0 for _ in range(n)] for _ in range(n)]

    ##바이러스가 놓인칸은 3으로 표시
    for x,y in start_node:
        test_graph[x][y] = 3
        visited[x][y] = 1
    
    temp_value = bfs(start_node,visited,test_graph)

    temp_check = check_graph(test_graph)

    if temp_check == True:
        min_time = min(min_time,temp_value)


if min_time == 3000:
    print(-1)

else:
    print(min_time - 3)