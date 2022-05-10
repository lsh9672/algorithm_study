#백준 5014번
import sys
from collections import deque

#최대 층, 현재 층, 목표 층, 위, 아래
f,s,g,u,d = map(int,sys.stdin.readline().split())

dir = [u,(-1)*d]


def bfs(start_node:int)->int:

    visited = set()

    need_visited = deque()

    need_visited.append([start_node,0])

    visited.add(start_node)

    while need_visited:

        current_node,current_count = need_visited.popleft()

        if current_node == g:
            return current_count

        
        for i in range(2):
            next_node = current_node + dir[i]

            if (0 < next_node <= f) and next_node not in visited:

                need_visited.append([next_node,current_count+1])
                visited.add(next_node)

    return -1

temp = bfs(s)

if temp == -1:
    print("use the stairs")

else:
    print(temp)