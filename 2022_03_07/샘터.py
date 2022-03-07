#백준 18513번 (샘터, 골드5, 그래프)
import sys
from collections import deque


#샘터, 집의 개수
n,k = map(int,sys.stdin.readline().split())

start_node_list = list(map(int,sys.stdin.readline().split()))

def bfs(start_node,k)-> int:

    next_node_cal = [-1,1]

    visited = dict()

    need_visited = deque(list())


    for i in start_node:
        visited[i] = 1
        need_visited.append([i,0])

    total_count = 0


    while need_visited:

        current_node, current_count = need_visited.popleft()

        if k==0:
            break

        for i in next_node_cal:
            next_node = current_node + i

            if next_node not in visited and k > 0:
                visited[next_node] = 1
                need_visited.append([next_node,current_count+1])
                total_count += current_count+1
                k -= 1

    return total_count

print(bfs(start_node_list,k))