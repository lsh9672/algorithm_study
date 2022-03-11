#백준 7569번(토마토, 골드5)
import sys
from collections import deque

#y,x,z
m,n,h = map(int,sys.stdin.readline().split())

# graph = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
graph = [list() for _ in range(h)]

for i in range(h):
    for _ in range(n):
        graph[i].append(list(map(int,sys.stdin.readline().split())))


def bfs(start_node:list):

    #가장 큰 일수 세기
    count = -1

    #상하좌우앞뒤
    dx = [-1,1,0,0,0,0]
    dy = [0,0,-1,1,0,0]
    dz = [0,0,0,0,-1,1]
    
    need_visited = deque(start_node)

    while need_visited:
        current_z,current_x, current_y  = need_visited.popleft()

        if graph[current_z][current_x][current_y] > count:
            count = graph[current_z][current_x][current_y]

        for k in range(6):
            next_z = current_z + dz[k]
            next_x = current_x + dx[k]
            next_y = current_y + dy[k]

            if (0<= next_z < h) and (0<= next_x < n) and (0<= next_y < m) and graph[next_z][next_x][next_y] == 0:
                graph[next_z][next_x][next_y] = graph[current_z][current_x][current_y] + 1
                need_visited.append([next_z,next_x,next_y])

    return count


start_node = list()

#모든 토마토가 익어있을때 확인
zero_check = False

for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 1:
                start_node.append([z,x,y])

            elif graph[z][x][y] == 0:
                zero_check = True

#0이 하나도 없음, 즉 전부 익어있음
if zero_check == False:
    print(0)
    

else:

    temp = bfs(start_node)
    #탐색이 끝났는데 안 익은게 있는지 반복문으로 돌면서 확인.
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if graph[z][x][y] == 0:
                    print(-1)
                    exit()
    
    print(temp-1)


    