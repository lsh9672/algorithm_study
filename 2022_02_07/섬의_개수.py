#백준 알고리즘 - 4963번 (그래프, 실버2)

'''아이디어'''
#1.각 좌표평면상의 한칸을 노드로 보게되면 이는 격자형 그래프가 된다.
#2. 시작노드를 (0,0)으로 잡고 bfs 탐색을 한다.
#4. 이때 인접노드는 가로,세로,대각선으로 한칸떨어져 있고 땅인 것이 노드이다.
#5. 탐색시에 탐색하는 땅들은 전부 0으로 처리해서 다음 탐색에서 방문안하도록한다.
#6  반복문을 돌면서 땅인부분(1)이 있으면 그 점에서 bfs탐색을 한다.

import sys
from collections import deque

#bfs 함수 정의 - graph를 반환해서 업데이트함, 탐색시작노드는 좌표이므로 튜플로 받음

def bfs(start_node:tuple, graph:list) -> list:

    #상하좌우 대각선
    dx = [ 0,0,-1,1,-1,-1, 1, 1]
    dy = [-1,1, 0,0,-1, 1,-1, 1]

    #따로 방문체크할 노드가 필요없음, 지도를 보면서 탐색하면 0으로 바꿀것이므로 지도에 방문체크가 이루어짐
    
    #다음 탐색이 필요한 노드 저장
    need_visited = deque(list())

    #시작노드를 넣음
    need_visited.append(start_node)
    
    #시작노드 방문처리
    graph[start_node[0]][start_node[1]] = 0

    #탐색 시작
    while need_visited :

        #높이와 넓이 - 행과 열
        current_h,current_w = need_visited.popleft()

        for i in range(len(dx)):
            next_h = current_h + dx[i]
            next_w = current_w + dy[i]

            #지도의 크기를 넘어가지 않으면 추가
            if next_h >= 0 and next_h < len(graph) and next_w >= 0 and next_w <len(graph[0]):

                #다음에 탐색할 위치가 땅(1)이면 추가
                if graph[next_h][next_w] == 1:

                    #방문처리
                    graph [next_h][next_w] = 0
                    #다음 탐색을 위해 추가
                    need_visited.append((next_h,next_w))
    
    return graph

while True:
    #지도의 너비(w)와 높이(h)
    w,h = map(int,sys.stdin.readline().split())

    #둘다 0이면 종료
    if w == 0 and h == 0:
        break
    #지도
    graph = list()

    

    for _ in range(h):
        #지도를 만듦
        temp = list(map(int,sys.stdin.readline().split()))
        graph.append(temp)

    count = 0
    #반복문을 돌면서 땅인부분(1)을 찾게 되면 그 점부터 bfs탐색을 함.
    for i in range(h):
        for j in range(w):
            #지도가 1이면 그점부터 탐색시작
            if graph[i][j] == 1:
                graph = bfs((i,j),graph)
                #탐색이 끝나면 섬의 개수 +1
                count += 1

    print(count)


