#백준 16234번 (인구이동, 골드5)
'''아이디어'''
#1. 각 칸을 노드로 보면 그래프라고 생각할수 있다.
#2. 만들어진 그래프에서 bfs 탐색을 하면서, 국경을 개방 할수 있는지 확인한다.
#3. 확인한 좌표와, 노드 값을 같이 저장하고, 몇개의 노드가 이동이 가능한지 확인한다.
#4. bfs탐색을 통해서 이동이 가능한 좌표값과 노드값을 다 구했으면 (모든 노드의 합 )/노드개수를 구한다.
#5. 구한 좌표들에 구한 값을 채워 넣고, 그래프를 반환한다.
#6. 위의 과정을 진행할때, 이동가능한 노드의 개수가 0인 경우에는 그래프를 반환하지 않는다.

import sys
from collections import deque


n,l,r = map(int,sys.stdin.readline().split())

graph = list()

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

#False이면 인구이동이 더이상 없음, True이면 인구이동이 발생
def bfs(start_node)-> bool:

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]


    need_visited = deque(list())

    need_visited.append(start_node)

    visited[start_node[0]][start_node[1]] = True

    #마지막에 위치 업데이트를 위해 저장
    node_location_list = list()

    while need_visited:

        current_x, current_y = need_visited.popleft()

        node_location_list.append([current_x,current_y])

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if next_x >= 0 and next_x < n and next_y >= 0 and next_y < n and visited[next_x][next_y] == False:
                if l <= abs(graph[current_x][current_y] - graph[next_x][next_y]) and abs(graph[current_x][current_y] - graph[next_x][next_y]) <= r: 
                    visited[next_x][next_y] = True
                    need_visited.append([next_x,next_y])

    return node_location_list


#인구 이동 일수
move_count = 0

while True:
    
    #False이면 탐색안한곳, True이면 탐색한곳
    visited = [[False for _ in range(n)] for _ in range(n)]

    #아래 반복문을 다 돌았는데도 True이면, 반복 종료, 더이상 국경이동이 없음
    check  = True
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                temp_list = bfs([i,j])
                
                #국경을 열라면 최소 2개 이상필요.
                if len(temp_list) > 1:
                    check = False
                    
                    #이동후 각 칸의 인구수
                    people = 0

                    for a,b in temp_list:
                        people += graph[a][b]

                    people = people // len(temp_list)

                    #구한 인구수로 이동한 칸 업데이트
                    for a,b in temp_list:
                        graph[a][b] = people

    if check == True:
        print(move_count)
        break

    else:
        move_count+=1


