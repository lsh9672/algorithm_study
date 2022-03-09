#백준 13023번 ABCDE
import sys
sys.setrecursionlimit=10**6


n,m = map(int,sys.stdin.readline().split())

graph = {node:list() for node in range(n)}

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(n)]


def dfs(start_node:int,count:int):
    visited[start_node] =1

    if count == 5:
        print(1)
        exit()

    
    for node in graph[start_node]:
        if visited[node] == 0:
            visited[node] = 1
            dfs(node,count+1)

for i in range(n):
    dfs(i,1)

print(0)   

