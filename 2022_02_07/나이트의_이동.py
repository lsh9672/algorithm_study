#백준 알고리즘 7562번 - 나이트의 이동(실버2)

'''아이디어'''
#1. 주어진 체스판의 각 칸을 노드로 보면 격자형 그래프로 볼수 있다. 따라서  그래프 탐색알고리즘을 이용할수 있다.
#2. 시작노드(루트)가 정해져있는 트리로 생각할수 있고, 한 노드에서 다른 노드는 나이트가 이동할수 있는 8개의 칸이 된다.
#3. 시작노드로 부터 bfs탐색을 시작한다.
#4. 시작 count를 0으로 하고 다음 이동마다 체스판에 count를 증가시켜서 저장한다.
#5. 탐색하다 이동하기를 원하는 노드에 도착하면 탐색을 멈추고 count값을 출력한다.

import sys
from collections import deque


'''bfs 정의'''
#나이트의 시작노드와 도달하고자 하는 노드, 체스판 정보를 인자로 받음
def bfs(start_node:tuple,end_node:tuple,graph:list) -> int:

    #다음노드 이동
    dy = [-1,1,-1,1,2,2,-2,-2]
    dx = [2,2,-2,-2,-1,1,-1,1]

    #방문처리는 체스판에 하면되기 때문에 따로 처리용 리스트를 만들필요는 없음
    need_visited = deque(list())

    #시작노드 저장
    need_visited.append(start_node)

    #시작을 1로 했기 때문에 나중에 최종적인 값에 -1을 해주면 된다.
    graph[start_node[0]][start_node[1]] = 1

    #break로 반복문 둘다 빠져나갈수 없기 때문에 사용하는 변수
    check  = False

    #리턴할 횟수
    result = None
    #탐색시작
    while need_visited:
        #행, 렬
        current_y, current_x = need_visited.popleft()

        for i in range(len(dx)):
            next_y = current_y + dy[i]
            next_x = current_x + dx[i]

            #목적지 노드이면 바로 출력
            if next_y == end_node[0] and next_x == end_node[1]:
                result = graph[current_y][current_x] + 1
                check = True
                break

            if next_y >= 0 and next_y < len(graph) and next_x >= 0 and next_x < len(graph[0]):
                #이동할 위치가 0이면 방문안했으니까 이동
                if graph[next_y][next_x] == 0:
                    graph[next_y][next_x] = graph[current_y][current_x]+1
                    need_visited.append((next_y,next_x))

        
        if check == True:
            break

    #시작을 1로 했기 때문에 최종적으로 -1함
    return result-1


'''입력'''
#테스트 케이스
test_case = int(sys.stdin.readline())

for _ in range(test_case):

    #체스판의 크기 - 체스판은 정사각형
    graph_size = int(sys.stdin.readline())

    #체스판 생성
    graph = [[0 for _ in range(graph_size)] for _ in range(graph_size)]

    #출발지
    start_node = tuple(map(int,sys.stdin.readline().split()))

    #도착지
    end_node = tuple(map(int,sys.stdin.readline().split()))

    if start_node == end_node:
        print(0)
        continue

    print(bfs(start_node,end_node,graph))
    




