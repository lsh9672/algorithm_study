# 백준 2252번 (골드3, 위상정렬)
import sys
from collections import deque


n,m = map(int,sys.stdin.readline().split())

graph = [list() for _ in range(n+1)]

## 진입차수 저장
indegree = [0 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())

    graph[a].append(b)

    indegree[b] += 1


def topology_sort(start_node:list)->list:

    people_order = list()

    need_visited = deque(start_node)

    while need_visited:

        current_node = need_visited.popleft()

        people_order.append(current_node)


        for i in graph[current_node]:
            indegree[i] -= 1

            if indegree[i] == 0:
                need_visited.append(i)

    return people_order

start_node = list()

for i in range(1,n+1):
    if indegree[i] == 0:
        start_node.append(i)

print(*topology_sort(start_node))


