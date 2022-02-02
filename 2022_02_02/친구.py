#백준 1058(그래프)
#간선의 가중치를 1로 두면 1인경우와 2인 경우가 2-친구 이다.
import sys
from collections import deque


'''입력'''
n = int(sys.stdin.readline())

#그래프 만들기(인덱스가 노드 - 0,1,2....)
graph = [list(map(str,sys.stdin.readline().strip())) for _ in range(n)]

def bfs(start_node,graph):

    visited = [False] * len(graph)

    need_visited = deque(list())
    need_visited.append([start_node,0])

    visited[start_node] = True

    #간선의 가중치를 1로 생각하고 1,2이면 숫자를 세서 저장할 변수
    friend_count = 0

    while need_visited:
        current_node,current_count = need_visited.pop()

        #가중치가 2보다 크면 2-친구가 아님
        if current_count > 2:
            continue
        
        #연결된 노드의 갯수가 같기 때문에 반복문을 돌려가면서 처리함
        #반복문을 돌면서 탐색을 한 노드가 아니고, Y(친구)이면 count값을 증가시키고 다음 탐색을 위해서 need_visited에 넣음
        for i in range(n):
            if visited[i] == False and graph[current_node][i] == "Y":
                friend_count += 1
                visited[i] = True
                need_visited.append([i,current_count+1])

    
    return friend_count

#가장 많은 친구수 출력
max = 0
#반복문을 돌면서 각 사람의 2-친구 수를 bfs탐색을 통해서 알아내고, 그중에 최대값을 저장해서 출력함
for i in range(n):
    #bfs탐색을 해서 2-친구 수를 찾음
    friend = bfs(i,graph)
    if max < friend:
        max = friend

print(max)




