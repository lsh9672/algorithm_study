# 백준 1012 유기농_배추
import sys
from collections import deque


def bfs(start_node:list, graph:list,m:int,n:int) -> list:

    #상하좌우 이동
    dx = [-1,1]
    dy = [-1,1]
    visited = list()

    need_visited = deque(list())

    need_visited.append(start_node)

    while need_visited:

        #탐색할 노드 꺼내기
        current_node = need_visited.popleft()

        if current_node not in visited:
            
            visited.append(current_node)

            #상하좌우값 넣기 - 인덱스 접근시 표를 벗어날수도 있으니 확인하고 넣기
            #상
            if current_node[0] - 1 >= 0:
                if graph[current_node[0] - 1][current_node[1]] == 1:
                    temp = (current_node[0]+dy[0],current_node[1])
                    need_visited.append(temp)

            #하
            if current_node[0] + 1 <= n-1:
                if graph[current_node[0] + 1][current_node[1]] == 1:
                    temp = (current_node[0]+dy[1],current_node[1])
                    need_visited.append(temp)

            #좌
            if current_node[1] - 1 >= 0:
                
                if graph[current_node[0]][current_node[1] - 1] == 1:
                    temp = (current_node[0],current_node[1]+dx[0])
                    need_visited.append(temp)

            #우
            if current_node[1] + 1 <= m-1:
                if graph[current_node[0]][current_node[1] + 1] == 1:
                    temp = (current_node[0],current_node[1]+dx[1])
                    need_visited.append(temp)

    return visited


result = list()

#입력
test_case_num = int(sys.stdin.readline())


for _ in range(test_case_num):

    #애벌레 수
    larva = 0
    
    #배추밭 정보 - 가로, 세로, 배추 위치 갯수
    m,n,k= map(int,sys.stdin.readline().split())

    #배추밭
    field = [[0 for _ in range(m)] for _ in range(n)]

    #배추위치
    cabbage_location = list()

    for _ in range(k):
        temp = tuple(map(int,sys.stdin.readline().split()))
        field[temp[1]][temp[0]] = 1
        cabbage_location.append((temp[1],temp[0]))
    
    #bfs로 탐색
    check_list = set(cabbage_location)
    while check_list:
        start_node = list(check_list)[0]
        check_list = check_list - set(bfs(start_node,field,m,n))
        larva += 1
    
    result.append(larva)

for i in result:
    print(i)