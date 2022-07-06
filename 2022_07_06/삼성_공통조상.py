#SWEA 1248번 (D5)
import sys
from collections import deque

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_07_06/input (9).txt", "r")

T = int(input())

def bfs(start_node:int, graph:list,v:int):
    visited = [0 for _ in range(v+1)]

    need_visited = deque()
    need_visited.append(start_node)

    visited[start_node] = 1

    total_node = 1

    while need_visited:

        current_node  = need_visited.popleft()

        for i in graph[current_node]:
            if visited[i] == 0:
                need_visited.append(i)
                visited[i] = 1
                total_node +=1

    return total_node

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    v,e,first_node,second_node = map(int,sys.stdin.readline().split())

    ##각 노드의 부모를 저장
    parent_list = [i for i in range(v+1)]

    temp = list(map(int,sys.stdin.readline().split()))

    graph = [list() for _ in range(v+1)]

    for i in range(0,e*2-1,2):
        a = temp[i]
        b = temp[i+1]
        parent_list[b] = a
        graph[a].append(b)

    first_parent_list = list()
    second_parent_list = list()

    ##첫번째 노드의 부모 구하기.
    while first_node != parent_list[first_node]:
        first_parent_list.append(parent_list[first_node])
        first_node = parent_list[first_node]
        
    ##두번째 노드의 부모 구하기
    while second_node != parent_list[second_node]:
        second_parent_list.append(parent_list[second_node])
        second_node = parent_list[second_node]

    result_node = 1
    ## 공통 최소 노드 찾기
    while (len(first_parent_list) != 0 and len(second_parent_list) != 0) and first_parent_list[-1] == second_parent_list[-1]:
        
        result_node = first_parent_list[-1]

        first_parent_list.pop()
        second_parent_list.pop()

    result_tree_level = bfs(result_node,graph,v)


    print(f"#{test_case} {result_node} {result_tree_level}")
