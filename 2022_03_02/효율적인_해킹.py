#백준 1325번 효율적인해킹(실버1, 그래프)

'''아이디어'''
#1. 각 컴퓨터를 노드로 보고 , 여기서 말하는 신뢰할수 있다는 의미는 연결이 되어있다는 의미이다.
#2. 1번처럼 보면, 그래프로 생각할수 있다.
#3. 문제에서 구하고자 하는 것이, 한번에 가장 많은 컴퓨터를 해킹할수 있는 컴퓨터 번호라고 했다.
#4. 3번의 뜻은, 시작노드에서 탐색했을때, 가장 연결노드의 수가 많이 나오는 것을 말한다.
#5. 이 문제는 트리라고 볼수 있다. A가 B를 신뢰하면 B에서 A로는 갈수 있지만, 반대의 경우는 아니므로 트리라고 생각할 수 있다.
#6. 깊이 우선탐색으로 노드별로 다 탐색해보고 순위를 정하도록 할 것이다.

#딕셔너리를 쓰면 시간초과가 나는데, 아마 해시충돌로 인해서 속도가 느려져서 그런것같다.

import sys
from collections import deque


n,m = map(int,sys.stdin.readline().split())

#인덱스 1부터 쓰기
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())

    graph[b].append(a)

def bfs(start_node:int)->int:
    count = 0

    visited = [0 for _ in range(n+1)]
    # visited = dict()
    need_visited = deque(list())

    need_visited.append(start_node)
    visited[start_node] = 1

    while need_visited:

        current_node = need_visited.popleft()

        count += 1

        for i in graph[current_node]:
            if visited[i] == 0:
                visited[i]= 1
                need_visited.append(i)

    return count


result= [0 for _ in range(n+1)]

for i in range(1,n+1):
    result[i] = bfs(i)

max_value = max(result)

for i in range(1,n+1):
    if result[i] == max_value:
        print(i,end=" ")




