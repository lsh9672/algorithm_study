#백준 알고리즘 1697번 - 숨바꼭질(그래프,실버1)

'''아이디어'''

#1. 우선 수빈이의 현재 위치값을 시작노드로 보고, 1초를 간선의 가중치, 걸었을때 값과 순간이동했을떄 값을 인접노드로 보면 그래프로 생각할수 있다.
#2. 그래프를 미리 만들필요없이 bfs탐색에 첫 노드를 넣고, x-1,x+1,2*x의 값을 인접노드로 생성한다.
#3. 인접노드를 생성할때 마다 count값을 +1(초기값 0)해서 노드의 값과 같이 저장한다.
#4. 각 노드의 값을 계산해서 동생의 위치(k)와 같으면 그때 저장한 count값을 반환해주고, 동생의 위치에 도달한 값이 없으면 다음 탐색을 위해 큐에 넣는다.
#필요한 모듈 => sys: 입출력을 위한 모듈, deque : bfs 탐색에 필요한 모듈

#시도 - 처음에 메모리 오류가 나서 최대로 나올수 있는 수를 10만으로 한정시켜버렸다.
# 다른사람 코드 - 고수들 코드를 보니 그냥 +1 -1 *2의 경우를 그래프에 추가하지 않고, 목적지 노드값에 가까운값들을 % // 등으로 계산해서 넣는식으로 속도와 메모리를 줄였다.

import sys
from collections import deque


'''입력'''
#n:수빈이의 위치(탐색 시작 노드값), 동생의 위치(최종 목적지 값)
n,k = map(int,sys.stdin.readline().split())

#시간초과 안나도록 크기 제한 - 주어진 크기가 10만이므로 이를 안넘도록 함.
max = 100000

#둘다 같다면 0
if n == k:
    print(0)

else:
    # 시작, 끝값을 받고 목적지 도달에 걸린 시간 프린트
    #걸린 시간 카운트
    count = 0

    #key 값에 노드, value에 걸린 시간을 저장.
    visited = dict()

    need_visited = deque(list())

    need_visited.append([n,0])

    visited[n] = 0

    while need_visited:

        current_node , current_count = need_visited.popleft()

        #목적지 노드이면 count에 걸린시간 저장하고 반환 - 큐에 넣어서 탐색하기 때문에 가장 먼저 도달하는게 최소시간임
        if current_node == k:
                count = current_count
                break

        next_node_list = [current_node - 1,current_node + 1,current_node * 2]


        for next_node in next_node_list:

            #저장된 값이 없으면 추가
            if next_node not in visited:
                if next_node <= max:
                    visited[next_node] = current_count+1
                    need_visited.append([next_node,current_count+1])

    print(count)
    
