#백준 1753번(골드5, 그래프 이론)

'''아이디어'''
#1. 그래프가 주어지고, 시작 정점을 주어서, 시작 정점으로부터 각 정점 간의 최단거리를 구하는 문제이다
#2. 최단거리를 구하는 문제이므로, 다익스트라 알고리즘을 이용하여 구할수 있다.
#3. 다익스트라는 힙을 이용해서 구한다.

import sys
import heapq


INF = sys.maxsize

v,e = map(int,sys.stdin.readline().split())

k = int(sys.stdin.readline())

#다익스트라 알고리즘
def dijkstra(start_node):
    
    #시작노드(자기자신)은 0으로
    distances[start_node] = 0

    heapq.heappush(priority_queue,(0,start_node))

    while priority_queue:
        current_weight,current_node = heapq.heappop(priority_queue)

        #꺼낸 값이 이미 저장된 값보다 작은면 패스
        if current_weight > distances[current_node]:
            continue

        #인접노드 정보 꺼냄
        for adjacent_weight,adjacent_node in graph[current_node]:
            
            #인접노드의 거리 계산
            distance = current_weight+adjacent_weight

            #인접노드의 거리를 기존에 저장된 거리와 비교'
            if distance < distances[adjacent_node]:
                #더 가까우면 업데이트 하고, 다음 탐색할수 있게 큐에 넣음
                distances[adjacent_node] = distance
                heapq.heappush(priority_queue, (distance,adjacent_node))

#0은 안씀
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int,sys.stdin.readline().split())

    graph[a].append((c,b))

#각 노드들의 가중치정보를 저장해둘 힙 - [노드, 가중치]로 저장
priority_queue = []

#거리를 저장할 딕셔너리
distances = [INF]*(v+1)

dijkstra(k)

for i in range(1,v+1):

    print("INF" if distances[i] == INF else distances[i])