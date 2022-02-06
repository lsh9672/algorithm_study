#백준 11725 - 트리의 부모 찾기 - 그래프(실버2)
'''아이디어'''
#1. 주어진 값으로 트리를 만든다
#2. bfs탐색을 한다.
#3. 방문노드 리스트에는 인덱스를 노드번호로 하고, 부모노드를 값으로 넣는다.
#4. 반환된 리스트의 값을 순서대로 2부터 출력을 한다.
import sys
from collections import deque

'''입력'''
#노드의 개수
n = int(sys.stdin.readline())

#그래프 생성 - 인덱스를 1부터 쓰기 위해서 n+1개만큼 생성함.
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    #간선 정보를 입력받음
    a,b = map(int,sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)


#bfs함수 정의
def bfs(start_node,graph):

    visited = [0 for _ in range(len(graph))]

    need_visited = deque(list())

    #시작노드 넣기
    need_visited.append(start_node)

    visited[start_node] = 1

    while need_visited:

        current_node = need_visited.popleft()

        for i in graph[current_node]:
            #방문한 적이 없다면 탐색
            if visited[i] == 0:
                visited[i] = current_node
                need_visited.append(i)

    return visited

        
#탐색 결과
result = bfs(1,graph)

for i in range(2,n+1):
    print(result[i])

