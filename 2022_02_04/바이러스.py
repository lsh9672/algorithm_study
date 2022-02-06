#백준  2606 그래프 이론

'''아이디어'''
#1. 주어진 입력으로 그래프를 만든다
#2. 만들어진 그래프를 시작노드를 1로 하여 bfs탐색을 한다.
#3. 탐색이 다 끝나면 1에서 갈수 있는 노드들의 정보들이 나오게 된다.(연결되어있지 않은 노드는 탐색하지 않음)
#4. 방문한 노드들의 수를 구해서 반환한다.

import sys
from collections import deque

#총 노드 수
node_num = int(sys.stdin.readline())

#그래프 만들기 - 0번은 안쓰기 위해 node_num+1
graph = [[] for _ in range(node_num+1)]

#간선 수
n = int(sys.stdin.readline())

for _ in range(n):

    a,b = map(int,sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

#bfs함수
def bfs(start_node,graph):

    #방문 체크할 노드 - 이 또한 0번째를 안씀
    visited = [False for _ in range(len(graph))]

    need_visited = deque(list())

    need_visited.append(start_node)

    while need_visited:

        current_node = need_visited.popleft()

        #방문을 하지 않았다면
        if visited[current_node] == False:
            #방문처리함
            visited[current_node] = True
            #다음 탐색을 위해 인접노드를 need_visited에 넣음   
            need_visited.extend(graph[current_node])

    return visited


result = bfs(1,graph)

#True의 갯수를 세고 시작노드인 1은 빼야되니 -1을 해준다.
print(result.count(True)-1)

