## 백준 14567번(위상정렬, 골드5)
import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

##0번째 인덱스 사용안함
graph = [list() for _ in range(n+1)]

##진입차수 저장
indegree = [0 for _ in range(n+1)]

for _ in range(m):
    a,b  = map(int,sys.stdin.readline().split())

    graph[a].append(b)

    indegree[b]+=1

def topology_sort(start_node:list,indegree:list):

    visited = [1 for _ in range(n+1)]

    need_visited = deque(start_node)

    while need_visited:

        current_node = need_visited.popleft()

        for i in graph[current_node]:
            
            indegree[i] -= 1
        
            if indegree[i] == 0:
                need_visited.append(i)
                visited[i] += visited[current_node]

    return visited


start_node = list()

for i in range(1,n+1):
    if indegree[i] == 0:
        start_node.append(i)

result_list = topology_sort(start_node,indegree)

for i in range(1,len(result_list)):
    print(result_list[i],end=" ")
    


