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

'''다른 풀이(시간 초과) - 아래에서 방법1, 방법2로 나뉘는데, 방법2을 이용하면 해결가능
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

    return distances



result = -1

##방법 1(시간초과). 이 부분에서 모든 노드에 대해서 다익스트라로 거리를 구하는 것이 아닌, 리프노들 구해서 리프노드로 하는것이 좋다.
#리프 노드의 경우, 자식노드의 갯수가 1개여야 한다(부모만 저장되어야 함.)
#루트의 경우, 어쩔수 없이 탐색


##방법 2(통과). 루트로 부터 가장 먼 노드를 구함.
# 가장 먼 노드로부터 가장 먼노드를 구함.
temp = search(1)

far_start_node = temp.index(max(temp))


temp = search(far_start_node)

result = max(temp)

print(result)
'''

'''다른풀이 - 다익스트라 말고, dfs를 이용해서 탐색해보려고 한다.
리프노드에서 부터 탐색함. 
다익스트라를 이용하지 않아도 됨 - 최단거리를 구하는 문제가 아니기 때문에
'''

import sys

sys.setrecursionlimit(10**6)


n = int(sys.stdin.readline())


#[[[1,14],[2,15]]]
graph = [list() for node in range(n+1)]

for _ in range(n-1):
    x,y,weight = map(int,sys.stdin.readline().split())

    graph[x].append([y,weight])
    graph[y].append([x,weight])

#리프노드 구하기
leaf_list = set()
for i in range(1,n+1):
    if len(graph[i]) == 1:
        leaf_list.add(i)

def dfs(start_node:int,current_wieght:int,distances:list):


    for next_node, next_weight in graph[start_node]:
        #-1이면 아직 방문안함
        if distances[next_node] == -1:
            distances[next_node] = next_weight + current_wieght
            dfs(next_node,next_weight + current_wieght, distances)

#0번째 인덱스는 안씀
distances = [-1 for _ in range(n+1)]

#자기자신은 0을 넣음
distances[1] = 0

#루트를 기준으로 가장 멀리갈수 있는 위치를 구함.(어떤노드던 상관없음)
dfs(1,0,distances)

#가장 멀리갈수 있는 노드를 추출

far_start_node = distances.index(max(distances))

#가장 멀리갈수 있는 노드에서 dfs해서 이 노드를 기준으로 가장 멀리가는 노드가 최대 길이가 됨.
distances = [-1 for _ in range(n+1)]

distances[far_start_node] = 0

dfs(far_start_node,0,distances)

print(max(distances))




