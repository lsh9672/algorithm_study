# 백준 9466번 (그래프, 골드3)

from itertools import cycle
import sys


sys.setrecursionlimit(10**6)

test_case = int(sys.stdin.readline())

def dfs(start_node:int,cycle_check) -> list:
    global team_success

    visited[start_node] = 1

    cycle_check.append(start_node)

    check_node = student_list[start_node]

    #탐색 끝났으면
    if visited[check_node] == 1:
        #싸이클 확인
        if check_node in cycle_check:
            team_success += cycle_check[cycle_check.index(check_node):]
        return
    
    else:
        dfs(check_node,cycle_check)


for _ in range(test_case):

    n = int(sys.stdin.readline())

    #1부터 사용
    student_list = [0] + list(map(int,sys.stdin.readline().split()))

    visited = [0 for _ in range(n+1)]

    team_success = list()

    for i in range(1,n+1):
        if visited[i] == 0:
            dfs(i,list())
    

    print(n - len(set(team_success)))

    
    

