#백준 2636번 치즈(골드5, 그래프)
'''아이디어'''
#1. 외벽에 있는 치즈를 녹여야 하므로 0,0부터 시작해서 bfs탐색을 한다.
#2. 격자판의 가장자리 한칸부분에는 치즈가 놓이지 않는다 했기 때문에 0,0은 빈칸이다
#3. 탐색을 하면서 인접노드가 1이면, count 값을 증가시키고, 해당 인접노드를 0으로 바꿔준다.
#4. 1이었던 인접노드는 0으로만 바꾸고, 다음 탐색을 위한 큐에는 넣지 않는다.
#5. 큐에는 넣지 않지만, 다른 빈칸에서 탐색할것을 대비해서 방문처리를 해둔다.
#6. 탐색이 끝나면 인덱스를 초로 생각해서 count 값을 저장해둔다.
#7. 이 과정이 끝나면 치즈가 없을때까지 (count가 0이 나올때까지 반복한다.)
import sys
from collections import deque

#세로와 가로
n,m = map(int,sys.stdin.readline().split())

#치즈정보를 넣을 그래프(격자판 - 2차원리스트)
graph = []

#그래프 채우기
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split(" "))))


dx = [0,0,-1,1]
dy = [-1,1,0,0]

#bfs 함수
def bfs():
    
    #방문노드는 1로 처리
    visited = dict()

    #치즈 수 세기
    count=0
    
    #다음에 방문해야 될 노드
    need_visited = deque(list())
    need_visited.append((0,0))
    
    visited[(0,0)] = 1


    while need_visited:

        current_x,current_y = need_visited.popleft()

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            #격자 판을 넘어가지 않았거나, 방문한적이 없을때
            if 0 <= next_x < n and 0 <= next_y < m and (next_x,next_y) not in visited:
                
                #인접노드가 0이면 다음 탐색에 추가
                if graph[next_x][next_y] == 0:
                    need_visited.append([next_x,next_y])
                    visited[(next_x,next_y)] = 1

                #인접노드가 1이면 count+1을 하고, 방문처리를 함, 큐에는 넣지 않음
                else:
                    #다음 탐색을 위해 녹은 치즈를 0으로 만들어버림
                    graph[next_x][next_y] = 0
                    visited[(next_x,next_y)] = 1
                    count+=1
        
    return count

#인덱스는 시간-1, 값은 각 시간에 녹은 치즈의 수
result = list()

while True:

    temp = bfs()

    if temp == 0:
        break

    result.append(temp)

#치즈가 다 녹는데 걸린 시간
print(len(result))

#녹기 한시간 전 치즈
print(result[-1])


