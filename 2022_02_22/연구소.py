#백준 - 14502번 연구소(골드5,그래프이론)
'''아이디어'''
#아이디어가 잘 생각나지 않아서 아이디어만 찾아보았다.
#1. 주어진 격자는 격자형 그래프이다.
#2 따라서 그래프탐색알고리즘을 쓸수있다.
#3 처음에는 바이러스의 상하좌우에 0이 있으면 count를 해서 3개이하면 그부분을 막고 그게 아닌경우를 생각해보려고 했지만, 도저히 방법이 생각나지 않았다.
#4 결국 벽 3개를 세울수 있는 모든 경우의 수를 만들고, 각각의 경우마다 벽을 세워두고 바이러스를 bfs탐색을 하면서 퍼트리고, 0의 개수를 세면 되는 문제다.
#5 벽 3개의 경우의 수는 우선 0이 있는 좌표를 모두 구하고, 순서는 상관이 없고, 중복되면 안되니 조합을 이용한다.

#2차원 리스트를 복사하는데 deepcopy를 사용했는데 테스트 결과, 이방법은 slicing보다 10배정도 느렸다.
#따라서 slicing으로 다시 바꿔보겠다.


# from copy import deepcopy
import sys
from collections import deque
from itertools import combinations


n,m = map(int,sys.stdin.readline().split())

graph = []

#빈 공간 (0) 위치 좌표를 저장할 리스트
empty_space_list = list()

#바이러스 정보를 저장해둠
virus_list = list()


#입력받은 정보로 그래프를 만들면서, 0인 좌표를 저장함, 2인 좌표도 저장해둠
for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    for j in range(m):
        if temp[j] == 0:
            empty_space_list.append([i,j])
        elif temp[j] == 2:
            virus_list.append([i,j])
    graph.append(temp)

#3개의 벽을 세울 경우의 수
three_wall_location = list(combinations(empty_space_list, 3))



#주어진 격자형 그래프를 탐색할 bfs 함수 정의 - 2에서 출발하고, 0을 만나면 전부 2로 바꿔버림
def bfs(start_node:list,graph:list) -> list:

    need_visited = deque(list())
    for k in start_node:
        need_visited.append(k)

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while need_visited:

        current_x, current_y = need_visited.popleft()

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            
            #좌표평면을 벗어나지 않는지, 해당 위치 값이 0인지 확인
            if next_x >= 0 and next_x < n and next_y >= 0 and next_y < m and graph[next_x][next_y] == 0:
                graph[next_x][next_y] = 2
                need_visited.append([next_x,next_y])
    
    return graph

#deepcopy는 느리기 떄문에 2차원 리스트를 복사하는 함수를 만들어 쓴다.
def list_copy(graph:list)->list:
    temp = []

    for i in graph:
        temp.append(i[:])

    return temp
    

#주어진 그래프에서 0의 개수를 세는 함수
def count_zero(graph:list) -> int:
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count+=1
    return count

#최대가 되는 안전영역 찾기 
max = 0

for wall in three_wall_location:

    #완전히 복사
    # temp_graph = deepcopy(graph)
    temp_graph = list_copy(graph)


    #벽세우기
    for a,b in wall:
        temp_graph[a][b] = 1
    
    #벽 세운 그래프에서 바이러스 퍼트리기(bfs함수 돌리기)
    temp_graph = bfs(virus_list,temp_graph)

    #안전지대 개수 세기
    temp_count = count_zero(temp_graph)
    
    if temp_count > max:
        max = temp_count

print(max)