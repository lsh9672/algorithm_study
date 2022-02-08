# 백준알고리즘 1303번 전쟁-전투 (실버1 - 그래프이론)

'''아이디어'''
#1. 문제에서 병사정보를 좌표평면으로 주었다.
#2. 좌표평면의 각 칸을 노드로 보면 격자형 그래프로 볼수가 있다.
#3. 격자형 그래프로 보게되면 그래프 탐색 알고리즘을 사용할수 있다.
#4. 입력정보로 그래프를 만든다(2차원 배열)
#5. 격자형 그래프에서 0,0부터 반복문으로 한칸씩 돌면서 w또는 b이면 bfs 탐색을 한다.(bfs탐색에서 시작노드)
#6. 상하좌우로만 이어져있을때 인접한 노드로 생각해서 시작노드의 값이 w인지,b인지 확인해서 탐색하면서 같은 알파벳일때만 방문을 한다.
#7. 방문한 그래프는 방문처리를 하고(방문했으면 W,B둘다 아닌 C로 바꾼다.) 인접노드로 넘어갈때마다 +1을 해서 몇개의 노드를 방문했는지를 count해서 반환한다.
#8. 반환받은 값을 w,b 두 경우로 나눠서 변수를 만들고 제곱후에 해당 변수에 더한다(누적함)
#9. 5번에서 말한 반복이 끝나면, 8번에서 저장한 값을 출력한다.
# 필요한 모듈 => sys:빠른 입력을 위해서 필요 ,deque: bfs탐색을 할것이기 때문에 queue라이브러리가 필요

import sys
from collections import deque


'''입력'''

#n:가로, m: 세로
n,m = map(int,sys.stdin.readline().split())

#그래프 생성
graph = []

for _ in range(m):

    graph.append(list(sys.stdin.readline()))

#bfs 함수 정의
#start_node는 (x,y) =>(행,열)
def bfs(start_node:tuple,color:str)-> int:
    
    count = 1 

    #상하좌우만 인접한 것으로 침 - 대각선 x
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    need_visited = deque(list())

    need_visited.append(start_node)

    #방문처리
    graph[start_node[0]][start_node[1]] = "C"

    while need_visited:
        current_x,current_y = need_visited.popleft()

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            #그래프를 벗어나지 않고
            if next_x >=0 and next_x < m and next_y >= 0 and next_y < n:
                if graph[next_x][next_y] == color:
                    count+=1
                    graph[next_x][next_y] = "C"
                    need_visited.append((next_x,next_y))
    return count

'''로직'''
#W값 누적
white_count = 0

#B값 누적
blue_count = 0

#반복문을 이용해서 시작노드를 찾음
for i in range(m):
    for j in range(n):
        #C이면 방문한곳
        if graph[i][j] =="W":
            result = bfs((i,j),"W")
            white_count += result*result

        elif graph[i][j] == "B":
            result = bfs((i,j),"B")
            blue_count += result*result

print(white_count,blue_count)


