#백준 17135번 (시뮬레이션 연습) - 아래의 풀이는 30퍼에서 틀림(무조건 왼쪽부터 쏘게해서 걸리면 바로 해당 적을 죽이고 종료하게함)
#왼쪽을 쏘는건, 쏠수 있는 가장 가까운 적이 여럿일때, 왼쪽을 쏴야 되는데, 지금은 무조건 왼쪽을 쏘게 해줌
import sys
from itertools import combinations
from collections import deque


# 격자판 크기, 궁수의 사거리
n,m,d = map(int,sys.stdin.readline().split())

graph = list()

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

# 좌, 상, 우만 보면됨
dx = [0,-1,0]
dy = [-1,0,1]

#궁수가 놓인 위치에서 bfs 탐색을 하면서 사거리가 되면 죽임(0으로 만듦) - 병사를 죽였으면 1, 아니면 0
def bfs(start_node:list,test_graph:list())-> tuple:

    visited = [[0 for _ in range(m)] for _ in range(n)]


    need_visited = deque(list())
    need_visited.append(start_node)

    while need_visited:

        current_x,current_y,current_count = need_visited.popleft()

        #현재위치에 병사가 있으면 가장 가깝기 떄문에 죽이고 리턴
        if test_graph[current_x][current_y] >= 1:
            test_graph[current_x][current_y] += 1
            return (current_x,current_y)

        for i in range(3):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            #격자판을 안넘어가는지 확인, 방문했던 노드인지 확인
            if (0 <= next_x < n) and (0 <= next_y < m) and visited[next_x][next_y] == 0:
                
                #거리가 궁수의 사거리인지 확인
                # temp_distance = abs(next_x - current_x) + abs(next_y - current_y) + current_count
                temp_distance = current_count + 1
                if temp_distance <= d:
                    #사거리 안 이라면, 다음 탐색을 위해서 추가 
                    need_visited.append([next_x,next_y,temp_distance])
    return (-1,-1)
    

#궁수의 사격이 끝나고(한턴이 끝나고) 맨 아래줄에 병사가 남아있는지 체크
def game_over_check()-> bool:
    #궁수의 사격이 끝났는데, 병사가 마지막칸에 남아있으면,게임 끝
    if 1 in test_graph[-1]:
        return True
    
    return False

result = 0 

def graph_copy():
    temp = list()

    for i in range(n):
        temp.append(graph[i][:])
    
    return temp


#궁수 3명을 놓을 수 있는 경우의 수 - 궁수의 행은 n
archer_location = combinations(range(m),3)

for loc in archer_location:

    temp_count = 0

    test_graph = graph_copy()

    game_count = 0

    while True:
        # 죽은 궁수의 위치 표시
        ancher_die_loc = set()

        for i in loc:
            temp = bfs([n-1,i,1],test_graph)
            if temp != (-1,-1):
                ancher_die_loc.add(temp)


        temp_count += len(ancher_die_loc)


        #게임판에서 궁수 제거
        for x,y in ancher_die_loc:
            test_graph[x][y] = 0

        #병사들 한칸씩 전진
        test_graph.pop()
        test_graph.insert(0,[0 for _ in range(m)])
        game_count += 1

        if game_count == n:
            break

    #몇명죽었는지 체크
    result = max(result,temp_count)

print(result)
