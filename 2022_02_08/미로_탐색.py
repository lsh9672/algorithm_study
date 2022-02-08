#백준 알고리즘 2178번 -미로탐색(실버1 - 그래프탐색)

'''아이디어'''
#1. 문제에서 주어진 좌표평면(미로)의 각 칸을 노드로 보고 인접한 노드가 상하좌우로 이동가능한 칸으로 보면 그래프로 생각할수 있다.
#2. 그래프로 생각하면  시작노드(좌표평면상에서는 0,0 - 문제에서는 1,1로 말함)에서 갈수 있는 인접노드를 탐색하면서 목적지에 도달하면된다.
#3. bfs로 현재 위치에서 갈수 있는 노드(숫자가 1이상)를 탐색하고 이동시마다 현재위치의 값 +1 한 값을 저장해둔다.
#4. 이동시에는 해당 위치에 저장된 값과 현재노드의 값 +1한 값을 비교해서 저장된 값이 더 크면 이동, 작으면 이동하지 않는다.(최소값을 구하야되므로)
#5. 목적지(N-1,M-1 => 0,0에서 시작했으므로)에 도착하면 해당 값을 출력한다.
# 필요한 모듈 => sys: 입출력, deque: bfs구현에 다음에 탐색할 노드를 저장할 자료구조로 큐가 필요

import sys
from collections import deque


'''입력'''
#n:세로, m: 가로

n,m = map(int,sys.stdin.readline().split())

#그래프 생성
graph = []

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip())))


#bfs 정의 - 그래프 탐색이 다 끝나면 목적지 값을 리턴
def bfs(start_node:tuple,graph:list) -> int:

    #상하좌우 이동정의
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    #방문체크는 graph에 함(0이 아닌 수를 비교하는 식으로)
    need_visited= deque(list())

    need_visited.append(start_node)

    while need_visited:

        current_x,current_y = need_visited.popleft()

        if current_x == n-1 and current_y == m-1:
            break

        for i in range(4):

            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            #아래 로직에서 1이면 탐색안한것으로 생각하도록 했는데, 시작노드의 경우에 첫번째라서 값이 계속 1이므로 , 시작노드면 패스하도록 함.
            # if next_x == 0 and next_y == 0:
            #     continue

            #좌표평면을 벗어나지 않아야되고 갈수 있는 위치(0이 아니여야됨)여야됨
            if next_x >=0 and next_x < n and next_y >=0 and next_y < m and graph[next_x][next_y] >= 1:
                #현재노드+1값과 해당 노드의 값과 비교해서 현재노드+1값이 더 작으면 업데이트, 또는 1이면 아직 업데이트가 안됨.
                # if graph[current_x][current_y] + 1 < graph[next_x][next_y] or graph[next_x][next_y] == 1:
                if graph[next_x][next_y] == 1:
                    graph[next_x][next_y] = graph[current_x][current_y] + 1
                    need_visited.append((next_x,next_y))

        #방문한곳을 0으로 바꿔버리면 다른 노드에서 인접노드가 이 노드라고 해도 탐색하지 않음
        #해당노드는 인접노드 일 수도 있고, 여러번거친 노드일수도 있는데 인접노드 추가후에 값을 0으로 바꿔버리면 다음에 탐색을 안함.
        #즉 맨처음 갔을때가 최소값이기 때문에 탐색할 필요가 없음
        #이렇게 하면 시작노드가 1이라서 위에서 조건문을 하나 더 추가해서 continue하도록 한 로직도 필요 없어짐
        graph[current_x][current_y] = 0

    return graph[n-1][m-1]

start_node = (0,0)
print(bfs(start_node,graph))


