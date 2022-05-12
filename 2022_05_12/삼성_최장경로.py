#SWEA 2814번 (싸피,D3)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_12/sample_input (2).txt", "r")

def dfs(start_node:int, visited:set,count:int):
    global result

    visited.add(start_node)

    result = max(result,count)

    for i in graph[start_node]:

        if i not in visited:
            dfs(i,visited,count+1)
    
    visited.remove(start_node)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    result = 0

    n,m = map(int,sys.stdin.readline().split())

    graph = [list() for _ in range(n+1)]

    for _ in range(m):

        a,b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a) 

    
    for i in range(1,n+1):
        dfs(i,set(),1)


    print(f"#{test_case} {result}")