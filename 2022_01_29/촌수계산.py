#백준 2644 - 그래프 탐색
import sys
from collections import deque


def bfs(start_node,graph):

    #촌수 계산을 위한 카운트
    count = 0

    visited = dict()

    need_visited = deque(list())

    need_visited.append([start_node,count])

    while need_visited:

    
        #탐색을 하기 위해서 큐에서 하나 꺼냄
        current_node,current_count= need_visited.popleft()

        #방문한적이 없다면
        if current_node not in visited:
            visited[current_node] = current_count

            for i in graph[current_node]:
                need_visited.append([i,current_count+1])
    
        
        # 방문한적이 있으면 count값 비교
        elif visited[current_node] > current_count:

            visited[current_node] = current_count
            
            for j in graph[current_node]:
                need_visited.append([j,current_count+1])

    return visited


'''입력'''
#전체 사람의 수 
n = int(sys.stdin.readline())

#촌수 탐색 대상
start_node,end_node = map(int,sys.stdin.readline().split())

#입력받을 그래프 정보 수
m = int(sys.stdin.readline())

# 전체인원수만큼 그래프 틀 만들기
graph = {node:list() for node in range(1,n+1)}

for _ in range(m):
    first,second = map(int,sys.stdin.readline().split())

    graph[first].append(second)
    graph[second].append(first)


#bfs 탐색 결과
#탐색결과에 비교대상이 없으면 -1
result = bfs(start_node,graph)

print(f"result : {result}")

if end_node not in result:
    print(-1)

else:
    print(result[end_node])






