#백준 1743 - 음식물 피하기 (그래프)

'''아이디어'''

#1. 주어진 가로세로 정보로 통로정보를 위한 틀을 만든다(격자형그래프)
#2. 이 문제는 격자형그래프로 볼수 있으면, 그래프에서 연결요소를 구하는 문제에서 조금 응용한 문제라는 것을 볼수 있다.
#3. 격자형 그래프를 만들면 안의 값을 전부 0으로 채운다.
#4. 입력으로 주어진 음식물 좌표를 받아서 해당 좌표를 전부 1로 채운다.
#5. 해당 그래프를 (0,0)부터 반복문을 돌면서 해당 좌표를 시작노드로 하여 bfs탐색을 한다.
#6. 탐색시에는 1인곳만 탐색을 하면서 이동할떄마다 +1을 해서 크기를 계산한다.
#7. 탐색한 부분의 값은 전부 0으로 바꾼다.(시작노드를 정할때 1인 부분만 시작노드로 할것이므로 이미 탐색한 부분은 0으로 두어 시작노드로 선정되지 않도록 한다.)
#8. bfs탐색이 끝나면 크기를 반환하고 이를 저장하고 있다가, 다음 시작노드의 탐색 결과와 비교해서 더 큰쪽으로 업데이트 한다.
#9. 모든 탐색이 끝나면 저장한 음식물 크기 변수에는 가장 큰 값이 저장되어있을 것이고 이를 출력해주면 된다.

'''입력'''
import sys
from collections import deque


#n:세로길이, m: 가로길이, k: 음식물갯수
n,m,k = map(int,sys.stdin.readline().split())

#그래프 만들기 - 초기셋팅은 전부 0으로, 음식물을 입력받아서 채울것임
graph = [[0 for _ in range(m)] for _ in  range(n)]

#음식물 위치 정보 입력 - 0을 안쓰고 1,1부터 사용하는 좌표가 입력으로 들어온다.
#0번부터 쓰고 싶기 떄문에 각 좌표에 -1을 해서 넣어준다.
for _ in range(k):
    r,c = map(int,sys.stdin.readline().split())

    #음식물을 1로 표시함
    graph[r-1][c-1] = 1


#bfs함수 정의
def bfs(start_node:list) -> int:

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    need_visited = deque(list())

    need_visited.append(start_node)

    graph[start_node[0]][start_node[1]] = 0

    count = 0
    while need_visited:
        current_x, current_y = need_visited.popleft()

        count += 1

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if next_x >= 0 and next_x < n and next_y >= 0 and next_y < m and graph[next_x][next_y] == 1:
                graph[next_x][next_y] = 0
                need_visited.append([next_x,next_y])

        

    return count

#음식물의 최대사이즈
result_size  = 0

#bfs탐색을 할때 시작노드를 정함 - 1인것만
for i in range(n):
    for j in range(m):
        #0일때는 탐색 x
        if graph[i][j] == 1:
            temp = bfs([i,j])

            if result_size < temp:
                result_size = temp

print(result_size)


