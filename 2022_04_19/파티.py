#백준 1238번 (골드3, 그래프)
'''아이디어
되게 단순한 다익스트라로 최단거리를 구하는 문제다.
모든 노드를 시작노드로 잡고 다익스트라를 돌려서 최단거리를 구하면 된다.
'''
import sys
import heapq

INF = 1000001

## n: 마을 및 사람 수, m: 간선수, x : 목표 노드
n,m,x = map(int,sys.stdin.readline().split())

graph = {node:dict() for node in range(1,n+1)}

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())

    graph[a][b] = c


def dijkstra(start_node:int) -> list:

    #0번은 안씀
    distances = [INF for _ in range(n+1)]
    
    #자기 자신은 0
    distances[start_node] = 0

    priority_queue = []

    heapq.heappush(priority_queue,[0,start_node])

    while priority_queue:

        current_wieght,current_node = heapq.heappop(priority_queue)


        #저장된 값보다 꺼낸것이 크면 패스
        if current_wieght > distances[current_node]:
            continue


        for next_node,temp_wieght in graph[current_node].items():
            temp_distance = temp_wieght + current_wieght

            if distances[next_node] > temp_distance:
                distances[next_node] = temp_distance
                heapq.heappush(priority_queue,[temp_distance,next_node])

    return distances

#0번은 안씀
result = [0 for _ in range(n+1)]

temp_list = None

for start_node in range(1, n+1):
    if start_node == x:
        temp_list = dijkstra(start_node)

    else:
        result[start_node] = dijkstra(start_node)[x]

#각 값 더하기
for i in range(1,n+1):
    result[i] += temp_list[i]

print(max(result))

