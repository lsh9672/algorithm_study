#백준 알고리즘 11724번 - 연결요소의 갯수 (그래프)
'''접근방법'''
#1. 전체노드를 리스트에 넣는다
#2. 첫번째 노드(임의로 정함 - 리스트의 첫번째 값으로 함)부터 bfs탐색을 함
#3. 탐색이 끝나면 연결되어있는 노드들의 정보들이 리스트에 담김
#4. 전체 노드 리스트에서 탐색하여 나오는 노드 정보들을 빼고 연결요소 개수를 +1함
#5. 전체 노드 리스트가 남아있다면, 또 다른 연결요소가 존재한다는 뜻이므로 남은 리스트에서 임의의 값을 선택해서 bfs탐색을 돌림
#6. 이 과정을 전체 노드 리스트에 노드가 남아있지 않을때까지 반복함

'''입력'''
import sys
from collections import deque


#n:정점의 개수, m:간선의 개수
n,m = map(int, sys.stdin.readline().split())

#그래프 정보를 담을 리스트 - 인덱스를 1번부터 쓰기 위해서 n+1개로 만듦
graph = {node : list() for node in range(1,n+1)}

#탐색한 노드 표시를 위한 리스트
node_info = list(graph.keys())

#간선정보
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

#bfs 함수 정의
def bfs(start_node,graph):

    visited = dict()

    need_visited = deque(list())

    need_visited.append(start_node)

    while need_visited:

        current_node = need_visited.popleft()

        if current_node not in visited:
            visited[current_node] = 1
            need_visited.extend(graph[current_node])

    return set(visited.keys())

#연결요소 개수 측정
count=0

#전체 노드 리스트를 다 탐색할때까지 반복
while node_info:
    result = bfs(node_info[0],graph)

    #탐색한 노드들을 전체 노드 정보에서 빼고 다시 노드에 넣음
    node_info = list(set(node_info) - result)

    #연결요소의 갯수를 +1함
    count +=1

print(count)