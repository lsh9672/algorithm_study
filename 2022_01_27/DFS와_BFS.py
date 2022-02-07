#백준 1260 
from collections import deque
import sys


def bfs(start_node,graph):

    visited = dict()

    need_visited = deque(list())

    need_visited.append(start_node)

    while need_visited:

        current_node = need_visited.popleft()

        if current_node not in visited:

            visited[current_node] = True
            temp = sorted(graph[current_node])
            need_visited.extend(temp)

    return visited.keys()


def dfs(start_node,graph):

    visited = dict()

    need_visited = list()

    need_visited.append(start_node)

    while need_visited:

        current_node = need_visited.pop()

        if current_node not in visited:

            visited[current_node] = True
            temp = sorted(graph[current_node],reverse=True)
            need_visited.extend(temp)

    return visited.keys()

#정점수, 간선수, 정점번호
n,m,v= map(int,sys.stdin.readline().split())

#그래프
graph = {node:list() for node in range(1,n+1)}

for _ in range(m):

    first_node,second_node = map(int,sys.stdin.readline().split())

    graph[first_node].append(second_node)

    graph[second_node].append(first_node)

print(' '.join(map(str,dfs(v,graph))))
print(' '.join(map(str,bfs(v,graph))))







