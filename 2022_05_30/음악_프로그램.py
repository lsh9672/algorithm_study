#백준 2623번 (골드2, 위상정렬)
import sys
from collections import deque

'''입력'''
n,m = map(int,sys.stdin.readline().split())

graph = [set() for _ in range(n+1)]

## 진입차수
in_degree = [0 for _ in range(n+1)]

for _ in range(m):

    temp = list(map(int,sys.stdin.readline().split()))

    temp_num = temp[0]

    if temp_num > 1:

        for i in range(1,temp_num):
            a = temp[i]
            b = temp[i+1]

            if b not in graph[a]:
                graph[a].add(b)

                in_degree[b] += 1

## 위상정렬
def topology_sort(start_node:list,in_degree:list):


    need_visited = deque(start_node)

    result = list()

    while need_visited:

        current_node = need_visited.popleft()

        result.append(current_node)

        for i in graph[current_node]:

            in_degree[i] -= 1

            if in_degree[i] == 0:
                need_visited.append(i)
    
    return result

start_node = list()

for i in range(1,n+1):
    if in_degree[i] == 0:
        start_node.append(i)

temp = topology_sort(start_node,in_degree)

## 남은 진입차수들이 전부 0이 아니면 순서를 나열할수 없음
# check = True
# for i in in_degree:
#     if i != 0:
#         check = False
#         break
# if check == True:
#     for i in temp:
#         print(i)
# else:
#     print(0)

## 진입차수가 아닌, 결과의 수가 n이 아니면 나열불가
if len(temp) == n:
    for i in temp:
        print(i)
else:
    print(0)

