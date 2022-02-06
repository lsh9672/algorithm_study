#백준 케빈 베이컨의 6단계 법칙(그래프이론) - 실버1

import sys
from collections import deque


'''입력'''
#n:유저수, m:친구 관계수
n,m = map(int,sys.stdin.readline().split())

#그래프를 2차원 배열로 만듦 - 인덱스 노드번호로 사용할것인데, 주어진 노드가 1부터 시작하기 때문에 n+1개만큼 생성하고 0번째는 사용하지 않음
graph = [[] for _ in range(n+1)]

#간선정보를 받아서 그래프를 채워넣음
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

#그래프를 탐색할 bfs함수 정의
def bfs(start_node,graph):

    #방문확인할 리스트를 만듦 -> 방문을 하지 않으면 -1로 두고 방문을 하면 count값을 넣음
    visited = [-1]*len(graph)

    need_visited = deque(list())

    #초기값 넣기
    need_visited.append([start_node,0])

    while need_visited:

        current_node,current_count = need_visited.popleft()

        if visited[current_node] == -1:
            visited[current_node] = current_count
            
            for i in graph[current_node]:
                need_visited.append([i,current_count+1])

        else:
            if visited[current_node] > current_count:
                visited[current_node] = current_count

    return visited


min = [n+1,(6*n)+1]
for i in range(1,n+1):
    
    result = bfs(i,graph)
    print(f"resutl : {result}")

    #-1을 제외한 값을 더함
    total = 0
    for j in result:
        if j != -1:
            total += j

    
    print(f"number :{i}, total: {total}")
    
    if min[1] > total:

        min[0] = i
        min[1] = total

print(min[0])



    


