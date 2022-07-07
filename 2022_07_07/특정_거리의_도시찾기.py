#백준 18352번 (스트릭유지용)'
import sys
from collections import deque

n,m,k,x = map(int,sys.stdin.readline().split())

graph = [list() for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())

    graph[a].append(b)


def bfs(start_node:int):
    visited = [-1 for _ in range(n+1)]


    need_visited = deque()

    need_visited.append([start_node, 0])

    visited[start_node] = 0

    while need_visited:

        current_node, current_count = need_visited.popleft()

        for i in graph[current_node]:
            if visited[i] == -1:
                next_count = current_count + 1

                visited[i] = next_count
                need_visited.append([i,next_count])

            else:

                next_count = current_count + 1
                if visited[i] > next_count:

                    visited[i] = next_count
                    need_visited.append([i,next_count])
                
                
    print(visited)
    return visited


temp = [a for a,b in enumerate(bfs(x)) if b == k]



if len(temp) == 0:
    print(-1)

else:
    temp.sort()
    for i in temp:
        print(i)