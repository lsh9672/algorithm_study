#백준 22868번 (그래프, 골드3)
import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

##그래프 - 0번은 안씀
graph = [list() for _ in range(n+1)]

## 간선 정보
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)


start_node, end_node = map(int,sys.stdin.readline().split()) 

for i in range(1,n+1):
    graph[i].sort()

## start_count가 0이면 가는거 0보다 크면 되돌아 오는거
def bfs(start_node:int,end_node:int,visited:list,start_count:int):

    visited[start_node] = 0

    need_visited = deque()

    need_visited.append([start_node,start_count])

    while need_visited:

        current_node, current_count = need_visited.popleft()

        if current_node == end_node:
            ##갈때는 방문 경로만 구함
            if start_count == 0:
                break
            ## 돌아오는 길이라면 값을 출력
            return current_count

        for next_node in graph[current_node]:

            if visited[next_node] == -1:
                ##왔던 경로를 찾을 수 있게 이전노드값을 넣어줌
                visited[next_node] = current_node
                need_visited.append([next_node,current_count+1])

    
    ## 경로 출력
    path = [end_node]
    next_visited = visited[end_node]

    ##0이면 출발지점
    while next_visited != 0 :
        path.append(next_visited)
        next_visited = visited[next_visited]

    return path[:-1]

visited = [-1 for _ in range(n+1)]

start_path = bfs(start_node,end_node,visited,0)

visited = [-1 for _ in range(n+1)]

for i in start_path:
    visited[i] = 1

print(bfs(end_node,start_node,visited,len(start_path)))



