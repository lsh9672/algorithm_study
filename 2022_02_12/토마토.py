#백준 7576번 토마토(그래프 이론)

'''아이디어'''
#1. 토마토 박스의 각 칸들을 노드로 생각하면 그래프로 보고 탐색을 하면 되는 문제이다.
#2. 반복문을 돌면서 1의 위치(익은 토마토 위치)를 모두 찾아서 탐색해야될 큐에 넣는다.
#3. 인접노드로 이동할때 마다 박스에 현재노드값+1을 해서 며칠이 걸리는지를 탐색한다.(업데이트는 0일때만한다..)
#4. 탐색이 다 끝나면 0인것이 있는지 확인해서 있으면 -1을 반환한다.
#5. 만약 0인것이 없다면 값들중 최대값이 답이다.
#6. 처음 탐색시에 시작노드가 한개가 아니라 여러개가 들어간채로 시작할수 있을뿐 기본적인 bfs탐색이랑 다를것이 없다.

#필요한 모듈 => sys,deque
import sys
from collections import deque


'''입력'''
#m:가로칸, n: 세로칸 => (n,m)
m,n = map(int,sys.stdin.readline().split())

#토마토 박스 정보입력
graph = []

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split(" "))))

#bfs함수 정의
def bfs(need_visited:deque,graph:list)->list:

    #상하좌우 이동
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while need_visited:
        current_x, current_y = need_visited.popleft()

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if next_x >= 0 and next_x < len(graph) and next_y >= 0 and next_y < len(graph[0]):
                if graph[next_x][next_y] == 0:
                    need_visited.append((next_x,next_y))
                    graph[next_x][next_y] = graph[current_x][current_y] + 1

    return graph

#시작노드 만들기
need_visited = deque(list())

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            need_visited.append((i,j))

#탐색끝나면 탐색완료된 정보가 담긴 그래프 업데이트
graph = bfs(need_visited,graph)

#가장 큰값 찾기, 0이 존재하면 -1리턴
max = 0
check = False
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            check = True
            max = 0
            break
        elif graph[i][j] > max:
            max = graph[i][j]
    
    if check==True:
        break

print(max-1)

'''나중에 생각한 방법'''
# 방법은 동일한데, 탐색이 다 끝나고 다시 반복문을 돌기보다는, 처음에 시작노드를 만들기 위해서
# 반복문을 돌때, 0이면 +1해서 개수를 누적시켜두고, 1이면 탐색할 노드에 저장하는 방식으로 하면 좀더 효율적일수 있다.
# 0의 개수는 bfs탐색시에 0인 노드를 탐색하면 -1해서 탐색이 끝났을떄 이 값이 0보다 크면 안익은 토마토가 있다는 뜻, 즉 모두 익지못하는 상황이라는것이고
# 0이면 모든 토마토가 익었다는 뜻이다
# 여기에 탐색시에 +1되는 날짜를 저장하면서 더 큰값이 나오면 업데이트 하는식으로 가지고 있으면 탐색과 동시에 최소날짜를 구할수 있게 된다. 
