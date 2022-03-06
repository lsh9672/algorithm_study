#백준 2668번(숫자 고르기, 골드5, 그래프)

import sys

n = int(sys.stdin.readline())

#인덱스 1부터 사용
num_list = [0 for _ in range(n+1)]


for i in range(1,n+1):

    num_list[i] = int(sys.stdin.readline())



def dfs(start_node,visited):
    temp = list()

    visited[start_node] = 1

    temp.append(start_node)

    if visited[num_list[start_node]] == 0:
        temp += dfs(num_list[start_node],visited)

    return temp
    
result = list()

for i in range(1,n+1):
    visited = [0 for _ in range(n+1)]
    temp_list = dfs(i,visited)
    check_set = set()
    for j in temp_list:
        check_set.add(num_list[j])

    if check_set == set(temp_list):
        result+=temp_list

result = list(set(result))
result.sort()


print(len(result))

for i in result:
    print(i)

'''조금 수정해본 풀이 - bfs로 풀어봄'''
# 결론적으로 위의 dfs 풀이보다 느림

# import sys
# from collections import deque

# n = int(sys.stdin.readline())

# graph = dict()

# for i in range(1,n+1):
#     graph[i] = int(sys.stdin.readline())

# def bfs(start_node):
#     visited = dict()

#     need_visited = deque(list())
#     need_visited.append(start_node)

#     visited[start_node] = graph[start_node]

#     while need_visited:
#         current_node = need_visited.popleft()

#         if graph[current_node] not in visited:
#             need_visited.append(graph[current_node])
#             visited[graph[current_node]] = graph[graph[current_node]]
    
#     return visited

# result = list()

# for i in range(1,n+1):
#     temp_dict = bfs(i)
    
#     key_set = set(temp_dict.keys())
#     value_set = set(temp_dict.values())

#     if key_set == value_set:
#         result += list(key_set)

# result = list(set(result))
# result.sort()
# print(len(result))

# for i in result:
#     print(i)