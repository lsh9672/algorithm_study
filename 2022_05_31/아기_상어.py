#백준 16236번 (시뮬레이션, 골드3)
import sys
from collections import deque

n = int(sys.stdin.readline().strip())

field = list()

for _ in range(n):
    field.append(list(map(int,sys.stdin.readline().split())))

shark_location = None

## 상어의 크기  - 자기보다 작은 물고기만 먹을 수 있다.
shark_size = 2

## 상어의 크기와 같은 양을 먹어야 크기가 증가한다.
shark_size_count = 0

## 모든 먹이를 먹는데 드는 시간 저장
result = 0


## 반복문 돌면서 상어(9)위치 찾기
for i in range(n):
    check = True
    for j in range(n):
        if field[i][j] == 9:
            shark_location = [i,j]
            field[i][j] = 0
            check = False
            break
    if check == False:
        break
    

## 상어가 먹이를 찾아가는 방법은 bfs탐색을 한다.
## 현재 상어의 위치에서 bfs탐색을 하면서 먹을수 있는 먹이를 찾는다.
## 이때 위-왼-아래-오른쪽, 순으로 해서 문제에서 제시한 가까운 먹이를 먼저 먹고, 여러개이면 오른쪽을 먹고 그런물고기가 여러개이면 왼쪽에 있는것을 먹는다는 조건을 만족시킨다.
## 처음으로 먹을수 있는 먹이를 먹으면 해당 위치의 값을 0으로 만들고, bfs를 종료한다
## 종료시 해당 위치를 상어의 현재위치로 만들고 다시 bfs탐색을 돌린다.

##bfs 탐색시에 사용할 좌표  - 위,왼,오른쪽,아래 순으로 나열
dx = [-1,0,0,1]
dy = [0,-1,1,0]

## 각 노드에는 좌표와 해당 위치로 이동하는데 경과된 시간을 같이 저장한다.
## 처음 시작 노드는 0이다
## return : 상어의 위치
def bfs(start_node:list,graph:list)->list:

    global result
    global shark_size
    global shark_size_count

    visited = [[0 for _ in range(n)] for _ in range(n)]

    need_visited = list()

    need_visited.append(start_node + [0])

    ##시작노드 방문처리
    visited[start_node[0]][start_node[1]]

    while need_visited:

        need_visited.sort(key= lambda x : (x[2],x[0],x[1]))

        current_x, current_y, current_time = need_visited.pop(0)

        

        if graph[current_x][current_y] > 0 and graph[current_x][current_y] < shark_size:
            result += current_time
            shark_size_count += 1
            if shark_size == shark_size_count:
                shark_size += 1
                shark_size_count = 0

            graph[current_x][current_y] = 0
            return [current_x,current_y]
        
        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if 0<= next_x < n and 0 <= next_y < n and visited[next_x][next_y] == 0 and graph[next_x][next_y] <= shark_size:
                visited[next_x][next_y] = 1
                need_visited.append([next_x,next_y,current_time+1])

    return -1


while True:

    temp = bfs(shark_location,field)

    if temp == -1:
        break

    else:
        shark_location = temp

print(result)