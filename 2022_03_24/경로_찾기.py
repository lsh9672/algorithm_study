#백준 11403번 (경로찾기, 실버1, 그래프)

import sys
from collections import deque,defaultdict

n = int(sys.stdin.readline())

graph = defaultdict(list)

for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))

    for j in range(n):
        if temp[j] == 1:
            graph[i].append(j)


visited = [[0 for _ in range(n)] for _ in range(n)]

def bfs(start_node):
    
    need_visited = deque(list())

    need_visited.append(start_node)

    # visited[start_node][start_node] = 1

    while need_visited:

        current_node = need_visited.popleft()

        for i in graph[current_node]:
            if visited[start_node][i] == 0:
                visited[start_node][i] = 1
                need_visited.append(i)


for i in range(n):
    bfs(i)

for i in visited:
    print(*i)


'''플로이드 워셜로 푼 풀이 - python3으로 제출시 3배쯤 느림, pypy3이면 반복문이 많아서 그런지 약간 빠름(아주약간)
import sys

n = int(sys.stdin.readline().strip())

graph  = []

for _ in range(n):

    graph.append(list(map(int,sys.stdin.readline().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for x in graph:
    print(*x)

'''




