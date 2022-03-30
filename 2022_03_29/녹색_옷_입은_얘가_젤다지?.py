#백준 4485번 (파이썬 그래프- 다익스트라, 골드4)
import sys
import heapq

MAX = 150000

result = list()

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def search(n:int,graph:list)-> list:
    distances = [[MAX for _ in range(n)] for _ in range(n)]

    distances[0][0] = graph[0][0]

    priority_queue = list()

    heapq.heappush(priority_queue,[distances[0][0],0,0])

    while priority_queue:

        current_distance, current_x, current_y = heapq.heappop(priority_queue)

        
        #꺼낸거가 기존꺼보다 크면 패스
        if distances[current_x][current_y] < current_distance:
            continue
        

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if (0 <= next_x < n) and (0 <= next_y < n):

                temp_distance = current_distance + graph[next_x][next_y]

                if temp_distance < distances[next_x][next_y]:
                    distances[next_x][next_y] = temp_distance
                    heapq.heappush(priority_queue,[temp_distance,next_x,next_y])


    return distances



while True:
    n = int(sys.stdin.readline().strip())

    if n == 0:
        break

    graph = list()

    for _ in range(n):
        graph.append(list(map(int,sys.stdin.readline().split())))

    temp = search(n,graph)
    result.append(temp[n-1][n-1])


for i in range(len(result)):
    print(f"Problem {i+1}: {result[i]}")
