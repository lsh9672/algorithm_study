import sys
from collections import deque

test_case = int(sys.stdin.readline())

result = list()


## 위상정렬
def bfs(n:int,start_node:list,end_node:int,build_time_list:list,graph:list,indegree:list,visited:list) -> int:
    
    need_visited = deque(start_node)

    while need_visited:

        current_node = need_visited.popleft()

        for next_node in graph[current_node]:
            ##진입 차수 줄이기
            indegree[next_node] -= 1

            next_count = build_time_list[next_node] + visited[current_node]

            if visited[next_node] < next_count:
                visited[next_node] = next_count
            
            ##진입 차수가 0이 되면 큐에 넣기
            if indegree[next_node] == 0:
                need_visited.append(next_node)

    return visited[end_node]
    

for _ in range(test_case):
    #n: 건물 개수, k: 규칙의 총개수
    n,k = map(int,sys.stdin.readline().split())

    #인덱스를 1부터 쓰기 위해서
    build_time_list = [-1]+ list(map(int,sys.stdin.readline().split()))

    graph = [list() for _ in range(n+1)]

    visited = [0 for _ in range(n+1)]

    ## 진입 차수 계산
    indegree = [0 for _ in range(n+1)]
    for _ in range(k):
        a,b = map(int,sys.stdin.readline().split())

        graph[a].append(b)

        ##b로 들어오는 진입 차수가 하나 생긴거
        indegree[b] += 1

    end_node = int(sys.stdin.readline())

    ## 진입 차수가 0인것을 찾기
    start_node = list()

    for x in range(1,n+1):
        if indegree[x] == 0:
            start_node.append(x)
            visited[x] = build_time_list[x]


    # print(bfs(n,start_node,end_node,build_time_list,graph,indegree))
    result.append(bfs(n,start_node,end_node,build_time_list,graph,indegree,visited))

for i in result:
    print(i)