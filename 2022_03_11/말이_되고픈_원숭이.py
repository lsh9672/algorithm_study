#백준 1600번 말이 되고픈 원숭이
'''아이디어'''
# 이문제는 벽부수기와 비슷한 유형으로 볼수 있다.
#.방문여부를 3차원 리스트로 해서 특수이동을 썼을때 안썼을때로 나눠서 계산해야된다.


import sys
from collections import deque


k = int(sys.stdin.readline())

#y,x
w,h = map(int, sys.stdin.readline().split())


graph = list()

for _ in range(h):
    graph.append(list(map(int,sys.stdin.readline().split())))

#K는 최대 30(0~30)
visited = [[[0 for _ in range(31)] for _ in range(w)] for _ in range(h)]

#일반이동 normal
nx = [0,0,-1,1]
ny = [-1,1,0,0]

#특수 이동 special
spx = [-1,-1,-2,-2,1,1,2,2]
spy = [-2,2,-1,1,-2,2,-1,1]


def bfs():

    need_visited = deque(list())
    need_visited.append([0,0,k])

    while need_visited:

        current_x,current_y,current_z = need_visited.popleft()

        #목표치에 도달하면 출력
        if current_x == h-1 and current_y == w-1:
            return visited[current_x][current_y][current_z]

        #먼저 일반이동을 한다.
        for i in range(4):
            next_x = current_x + nx[i]
            next_y = current_y + ny[i]

            #좌표를 벗어나지 않으면서, 장애물이 아니고 방문하지 않은 곳이라면(방문여부에서 특수이동은 그대로 둠, 일반이동이므로)
            if (0 <= next_x < h) and (0 <= next_y < w) and graph[next_x][next_y] != 1 and visited[next_x][next_y][current_z] == 0:

                visited[next_x][next_y][current_z] = visited[current_x][current_y][current_z]+1
                need_visited.append([next_x,next_y,current_z])


        #일반이동을 하고나서, 만약 k가 0보다 크면, 특수이동한 값도 저장한다.
        if current_z > 0 :
            for j in range(8):
                next_x = current_x + spx[j]
                next_y = current_y + spy[j]

                #좌표를 벗어나지 않으면서, 장애물이 아니고 방문하지 않은 곳이라면(방문여부에서 특수이동을 -1해야됨,)
                if (0 <= next_x < h) and (0 <= next_y < w) and graph[next_x][next_y] != 1 and visited[next_x][next_y][current_z -1] == 0:
                    
                    visited[next_x][next_y][current_z-1] = visited[current_x][current_y][current_z]+1
                    need_visited.append([next_x,next_y,current_z - 1])

    return -1


print(bfs())
