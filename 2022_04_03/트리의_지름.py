#백준 1967번 (그래프 연습, 골드4)

'''틀린 풀이 - 가중치가 있는 노드여서 다익스트라를 이용해서 구했다.
다익스트라로 구하게 되면, 이 문제의 경우, 모든 노드에 대해서 다익스트라를 돌리면서 거리를 구하기 때문에,
n^2(logn)으로 굉장히 느리게 나온다.(물론 플로이드 워셜보다는 낫다)

import sys
import heapq


n = int(sys.stdin.readline())

#도달할수 없는 값 정의
INF = 1000001

graph = {node:dict() for node in range(1,n+1)}

for _ in range(n-1):
    x,y,weight = map(int,sys.stdin.readline().split())

    graph[x][y] = weight
    graph[y][x] = weight



def search(start_node:int)->int:

    distances = [INF for _ in range(n+1)]

    distances[0] = -1

    distances[start_node] = 0

    priority_queue = list()

    heapq.heappush(priority_queue,[0,start_node])

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for next_node, temp_distance in graph[current_node].items():
            next_distance = distances[current_node] + temp_distance

            if next_distance < distances[next_node]:
                distances[next_node] = next_distance
                heapq.heappush(priority_queue,[next_distance,next_node])

    return max(distances)


result = -1
for i in range(1,n+1):
    temp = search(i)

    result = max(result, temp)

print(result)

'''

'''다른 풀이(시간 초과)
#모든 노드를 구하는 것이 아닌, 리프노드에서의 거리만 구하면 시간을 좀더 줄일수 있을것 같다.
#리프가 아닌 노드보다는 더 갈곳이 없는, 리프노드에서 하는것이 일반적으로 최대거리를 만들수 있기 때문에 리프노드에서 다익스라를 구한다.

#시간초과
#다익스트라의 경우, 한 노드에서 다른 노드로 가는 모든 경로에 대한 거리를 구하기 때문에 오버헤드가 큰것 같다.

import sys
import heapq


n = int(sys.stdin.readline())

#도달할수 없는 값 정의
INF = 1000001

graph = {node:dict() for node in range(1,n+1)}

for _ in range(n-1):
    x,y,weight = map(int,sys.stdin.readline().split())

    graph[x][y] = weight
    graph[y][x] = weight



def search(start_node:int)->int:

    distances = [INF for _ in range(n+1)]

    distances[0] = -1

    distances[start_node] = 0

    priority_queue = list()

    heapq.heappush(priority_queue,[0,start_node])

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for next_node, temp_distance in graph[current_node].items():
            next_distance = distances[current_node] + temp_distance

            if next_distance < distances[next_node]:
                distances[next_node] = next_distance
                heapq.heappush(priority_queue,[next_distance,next_node])

    return max(distances)



result = -1

##이 부분에서 모든 노드에 대해서 다익스트라로 거리를 구하는 것이 아닌, 리프노들 구해서 리프노드로 하는것이 좋다.
#리프 노드의 경우, 자식노드의 갯수가 1개여야 한다(부모만 저장되어야 함.)
#루트의 경우, 어쩔수 없이 탐색
leaf_list = list()
for i in range(1,n+1):
    if len(graph[i]) == 1:
        leaf_list.append(i)

for i in leaf_list:
    temp = search(i)

    result = max(result, temp)

print(result)
'''

'''다른풀이 - 다익스트라 말고, dfs를 이용해서 탐색해보려고 한다.
리프노드에서 부터 탐색함.
'''
import sys


n = int(sys.stdin.readline())

#도달할수 없는 값 정의
INF = 1000001

graph = {node:dict() for node in range(1,n+1)}

for _ in range(n-1):
    x,y,weight = map(int,sys.stdin.readline().split())

    graph[x][y] = weight
    graph[y][x] = weight

#리프노드 구하기
leaf_list = list()
for i in range(1,n+1):
    if len(graph[i]) == 1:
        leaf_list.append(i)

print(leaf_list)