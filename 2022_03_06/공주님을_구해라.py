#백준 17836번 (공주님을 구해라, 골드5)
'''아이디어'''
#1. 각 칸을 노드로 보면 그래프로 생각하고, 탐색알고리즘을 쓸수 있다.
#2. 이전에 푼 문제들과 동일하게, 벽이면 이동하지 않고, 벽이면 이동하게 한다.
#3. 조금 추가되는 점은, 검을 가지게 되면, 벽을 부술수 있다.
#4. 검을 획득하면 그때부턴 벽도 무시하고 부수면 된다.
#5. 검이 있으면, 벽부수는 횟수에 제한이 없으므로, 검을 얻은순간 목적지 까지 직선거리를 구하면 된다.
import sys
from collections import deque


n,m,t = map(int,sys.stdin.readline().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))


def bfs():

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    visited = [[0 for _ in range(m)] for _ in range(n)]
    
    need_visited = deque(list())
    need_visited.append([0,0])

    visited[0][0] = 1

    sword_value = 10001

    while need_visited:
        current_x,current_y = need_visited.popleft()

        #검을 구했으면 목적지까지 최단거리를 구함
        if graph[current_x][current_y] == 2:
            #검을 가지고 이동한 최단 거리.
            sword_value = visited[current_x][current_y] + abs(n-1 - current_x) + abs(m-1 - current_y)

        #목적지에 도달했으면, 검을 가지고 이동한 거리와 비교해본다.
        if current_x == n-1 and current_y == m-1:

            return min(visited[n-1][m-1]-1,sword_value-1)

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            #벽을 안넘어가는지 확인
            if next_x>=0 and next_x < n and next_y >= 0 and next_y < m and graph[next_x][next_y] != 1 and visited[next_x][next_y] == 0:
                visited[next_x][next_y] = visited[current_x][current_y]+1
                need_visited.append([next_x,next_y])

    return sword_value

time = bfs()

if time > t:
    print("Fail")

else:
    print(time)