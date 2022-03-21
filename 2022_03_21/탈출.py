#백준 3055번(골드4, 그래프연습)
import sys
from collections import deque

r,c = map(int, sys.stdin.readline().split())

graph = list()

start_node = None

end_node = None

water_node = list()

for i in range(r):

    temp = list(sys.stdin.readline().strip())
    
    #목적지
    if "D" in temp:
        end_node = [i,temp.index("D")]
    
    #시작위치
    if "S" in temp:
        start_node = [i,temp.index("S"),0]

    #물
    if "*" in temp:
        water_node.append([i,temp.index("*"),0])

    graph.append(temp)

#이동 정의
dx = [0,0,-1,1]
dy = [-1,1,0,0]


#물을 먼저 퍼트리기
def water_bfs():

    visited = [[-1 for _ in range(c)] for _ in range(r)]

    need_visited = deque(water_node)

    for a,b,m in water_node:
        visited[a][b] = 0

    while need_visited:

        current_x,current_y,current_count = need_visited.popleft()

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if (0 <= next_x < r) and (0 <= next_y < c) and visited[next_x][next_y] == -1 and graph[next_x][next_y] != "D" and graph[next_x][next_y] != "X":

                visited[next_x][next_y] = current_count + 1
                need_visited.append([next_x,next_y,current_count+1])

    return visited        


def bfs(water_visited:list):
    
    visited = [[-1 for _ in range(c)] for _ in range(r)]

    need_visited = deque(list())

    
    need_visited.append(start_node)

    visited[start_node[0]][start_node[1]] = 0


    while need_visited:

        current_x, current_y, current_count = need_visited.popleft()
        
        for i in range(4):

            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if (0 <= next_x < r) and (0 <= next_y < c) and visited[next_x][next_y] == -1 and graph[next_x][next_y] != "X":
                #목표지점이라면, 종료
                if next_x == end_node[0] and next_y == end_node[1]:
                    return current_count+1

                if graph[next_x][next_y] == "." and (water_visited[next_x][next_y] > current_count+1 or water_visited[next_x][next_y] == -1):
                    need_visited.append([next_x,next_y,current_count+1])
                    visited[next_x][next_y] = 1
                



    return -1


water_visited = water_bfs()


result = bfs(water_visited)

if result == -1:
    print("KAKTUS")

else:
    print(result)