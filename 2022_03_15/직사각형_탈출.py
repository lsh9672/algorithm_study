#백준 16973번 직사각형 탈출(그래프)
import sys
from collections import deque


n,m = map(int,sys.stdin.readline().split())

graph = list()

for _ in range(n):

    graph.append(list(map(int,sys.stdin.readline().split())))

#
h,w,start_x,start_y,stop_x,stop_y = map(int,sys.stdin.readline().split())

#0,0부터 시작하기 때문에 각 좌표에서 1씩 빼줌
start_x = start_x -1
start_y = start_y -1
stop_x = stop_x -1
stop_y = stop_y -1


graph[start_x][start_y] = 2

#상하좌우 이동 정의
dx = [0,0,-1,1]
dy = [-1,1,0,0]

'''시간초과 남
#현재 좌표값을 주면, 사각형의 높이와 넓이를 이용해서 벽인 부분이 있는지, 그래프를 넘어갔는지 확인함
#true이면 문제 없음
#false이면 문제 있음, 따라서 큐에 탐색할 노드로 추가하지 않음
#location_x,location_y는 사각형의 왼쪽위 좌표
def wall_check(location_x:int,location_y:int) -> bool:

    for i in range(location_x, location_x+h):
        for j in range(location_y,location_y+w):

            if i== location_x and j == location_y:
                continue

            if i < 0 or i >=n or j < 0 or j >= m or graph[i][j] == 1:
                return False
        

    return True
'''

wall_list = list()

#벽의 좌표를 미리빼두고, 사각형 내부에 벽이 있는지, 반복문을 돌면서 계산하는 것이 아니라, 좌표값의 크기로 비교
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            wall_list.append([i,j])
        

def wall_check(location_x:int,location_y:int)->bool:

    #사각형이 맵 밖으로 벗어나면 안됨.
    if location_x + h-1 >=n or location_y + w-1 >=m:
        return False 

    for x,y in wall_list:
        if (location_x <= x < location_x + h ) and (location_y <= y < location_y + w):
            return False

    return True 


#시작점을 2로 두어서, 벽(1)과 겹치치 않게 한다. - 마지막에 -2해주면 됨.
def bfs():

    need_visited = deque(list())

    need_visited.append([start_x,start_y])

    while need_visited:

        current_x, current_y = need_visited.popleft()

        if current_x == stop_x and current_y == stop_y:
            return graph[current_x][current_y] - 2

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            #직사각형의 왼쪽위의 점을 이동시킬수 있는지 확인.+ 직사각형의 나머지 부분이 벽이 아닌지, 그래프를 벗어나지 않았는지 확인
            if (0 <= next_x < n) and (0 <= next_y < m) and graph[next_x][next_y] == 0 and wall_check(next_x,next_y) == True:
                need_visited.append([next_x,next_y])
                graph[next_x][next_y] = graph[current_x][current_y] + 1

            
    return -1

print(bfs())
    





