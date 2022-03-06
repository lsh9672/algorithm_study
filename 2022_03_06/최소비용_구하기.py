#백준 1916번 (최소비용구하기 골드5)
#초반에 틀렸던 이유 - 처음에는 시작에서 도착지점으로 가는 버스가 한개씩 주어진다고 생각해서 계속틀림
# 동일한 시작지점에서 동일한 도착지점으로 가는데, 가중치가 다른 버스가 존재함(1,2,10 / 1,2,20)
import sys
import heapq


INF = 100000001
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

#0번째는 안씀
graph = [[] for _ in range(n+1)]

#그래프 채우기
for _ in range(m):
    #출발점, 도착점, 버스비용
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append([b,c])

start_node,end_node = map(int,sys.stdin.readline().split())

#반환값으로 비용을 반환.
def dijkstra(start_node:int,end_node:int)-> int:

    #인덱스 0은 안씀
    visited = [INF for _ in range(n+1)]

    #자기자신은 0으로 함
    visited[start_node] = 0

    priority_queue = []

    heapq.heappush(priority_queue,[visited[start_node],start_node])

    while priority_queue:
        current_distance,current_node = heapq.heappop(priority_queue)

        #큐에서 꺼낸거보다 이미 저장된 거리가 더 짧으면 패스
        if current_distance > visited[current_node]:
            continue
        
        #인접노드와 가중치를 꺼냄
        for next_node,temp_distance in graph[current_node]:

            next_distance = current_distance + temp_distance

            if visited[next_node] > next_distance:

                visited[next_node] = next_distance
                heapq.heappush(priority_queue,[next_distance,next_node])

    return visited[end_node]


print(dijkstra(start_node,end_node))

    

