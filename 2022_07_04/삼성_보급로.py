##swea 1249번 (D4)
import sys
import heapq

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_07_04/input (1).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

##상하좌우 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start_node:list,n:int,graph:list)-> int:
    visited = [[-1 for _ in range(n)] for _ in range(n)]

    need_visited = list()
    heapq.heappush(need_visited,[0]+start_node)

    visited[start_node[0]][start_node[1]] = 0

    while need_visited:

        current_count,current_x,current_y = heapq.heappop(need_visited)
        

        if visited[current_x][current_y] < current_count:
            continue

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if (0 <= next_x < n) and (0 <= next_y < n):
                ## 다음 노드가 탐색안한 곳이면 그냥 업데이트
                if visited[next_x][next_y] == -1:
                    visited[next_x][next_y] = current_count+ graph[next_x][next_y]
                    heapq.heappush(need_visited,[visited[next_x][next_y],next_x,next_y])
                    

                ## 다음 노드가 탐색한 곳이라면 둘 중 작은 값으로 업데이트
                elif visited[next_x][next_y] > current_count+ graph[next_x][next_y]:
                    visited[next_x][next_y] = current_count+ graph[next_x][next_y]
                    heapq.heappush(need_visited,[visited[next_x][next_y],next_x,next_y])

                

    return visited[n-1][n-1]

for test_case in range(1, T + 1):
    
    result = 0

    n = int(sys.stdin.readline().strip())

    graph = list()

    for _ in range(n):
        graph.append(list(map(int,list(sys.stdin.readline().strip()))))

    result = bfs([0,0],n,graph)
    
    print(f"#{test_case} {result}")