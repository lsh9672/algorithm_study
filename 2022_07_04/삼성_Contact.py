#SWEA 1238번 (D4, 사전 과제)
import sys
from collections import deque


sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_07_04/input (3).txt", "r")

def bfs(start_node:int,graph:dict)-> int:

    visited = dict()

    need_visited = deque()
    need_visited.append([start_node,0])

    visited[start_node] = 0


    while need_visited:

        current_node,current_count = need_visited.popleft()

        result = current_node
        

        for i in graph[current_node]:
            if i not in visited:
                need_visited.append([i,current_count+1])
                visited[i] = current_count+1

    return visited

# T = int(input())
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n, start_node = map(int,sys.stdin.readline().split())

    temp = list(map(int,sys.stdin.readline().split()))

    graph = dict()

    for i in range(0,n-1,2):
        a,b = temp[i], temp[i+1]

        if a in graph:
            graph[a].append(b)

        else:
            graph[a] = [b]

        
        if b not in graph:
            graph[b] = []
    
    temp = bfs(start_node,graph)

    temp = list(temp.items())

    temp.sort(key=lambda x: (x[1],x[0]))


    print(f"#{test_case} {temp[-1][0]}")