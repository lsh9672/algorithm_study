#백준 16954번 (움직이는 미로탈출)
'''아이디어'''
#처음에 생각을 했는데, 기존 bfs와 약간 다른 유형이라 감을 못잡아서 구글링을 통해 아이디어를 얻었다.
#bfs에서 한번만 더 생각해보면 되는것이었다.
#벽이 내려온다는 것은, 매 탐색마다, graph가 새롭게 초기화 된다고 생각하면 된다.
#이동후에, 벽을 업데이트하고,현재 위치가 벽의 위치가 아닌지 확인하는 식으로 탐색을 한다.
#현재 위치로 부터 갈수 있는 노드 즉, 1초동안 이동할수 있는 노드를 전부 구하고, 벽을 이동시킨후에 비교해본다.
import sys
from collections import deque

graph = []

for _ in range(8):
    graph.append(list(map(str,sys.stdin.readline().strip())))

##출발: [7,0]
##도착:[0,7]

def bfs():
    dx = [0,0,0,-1,1,-1,1,-1,1]
    dy = [0,-1,1,0,0,1,-1,-1,1]

    need_visited = deque(list())
    need_visited.append([7,0])

    while need_visited:
        #방문처리 - 매초마다 초기화해서 써야됨'
        visited = [[0 for _ in range(8)] for _ in range(8)]
        #1초간 들어있는 노드(위치)를 탐색하면서, 벽에 충돌하는지 확인.
        for _ in range(len(need_visited)):
            current_x,current_y = need_visited.popleft()

            #만약 해당 노드가 목적지라면 1을 리턴
            if current_x == 0 and current_y == 7:
                return 1

            #만약 해당위치가 벽이라면 다음탐색
            if graph[current_x][current_y] == "#":
                continue

            #다음탐색을 위한 인접 노드 추가
            for i in range(9):
                next_x = current_x + dx[i]
                next_y = current_y + dy[i]

                #게임판을 벗어나지 않고, 벽이 아니면 방문큐에 추가.+ 방문확인
                if (0<=next_x<8) and (0<=next_y<8) and graph[next_x][next_y] == "." and visited[next_x][next_y] == 0:
                    visited[next_x][next_y] = 1
                    need_visited.append([next_x,next_y])
            
        #1초간의 이동이 끝나면 벽을 이동 - 맨 아래 벽빼고, 맨 첫번째에 빈 공간 한줄을 넣는다.
        graph.pop()
        graph.insert(0,[".",".",".",".",".",".",".","."])

    return 0

print(bfs())