#백준 알고리즘 - 상근이의 여행 9372(그래프)
import sys
from collections import deque

#이 문제는 사실 노드갯수 -1 이다
#국가를 노드로 보고 비행기 타는 경우를 간선으로 보면, 그래프가 링크드리스트처럼 이어져이어서, 모든 노드를 방문하는 최단경우는 모든간선을 한번씩 거치는 경우, 즉 노드-1이다


def bfs(start_node, graph):

    visited = [False for i in range(len(graph))]

    count = 0

    need_visited = deque(list())

    need_visited.append(start_node)

    visited[start_node] = True

    while need_visited:

        current_node = need_visited.popleft()

        for i in graph[current_node]:
            if visited[i] == False:
                visited[i] = True
                count += 1
                need_visited.append(i)

    return count


test_case = int(sys.stdin.readline())

for _ in range(test_case):

    n,m = map(int,sys.stdin.readline().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        
        a,b = map(int,sys.stdin.readline().split())

        graph[a].append(b)
        graph[b].append(a)

        
    result = bfs(1,graph)
    print(result)
