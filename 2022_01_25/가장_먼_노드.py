#ㅍ로그래머스 level3 가장 먼 노드
'''각 노드에 가중치를 모두 1로 생각하면 다익스트라 알고리즘이 된다.'''
import heapq

#다익스트라
def dijkstra(start_node:int,graph:dict) -> dict:

    distances = {node:float('inf') for node in graph}

    distances[start_node] = 0

    priority_queue = []

    heapq.heappush(priority_queue,[start_node,distances[start_node]])

    while priority_queue:
        
        current_node,current_distance =  heapq.heappop(priority_queue)

        if distances[current_node] < current_distance:
            continue
            
        for adjacent,weight in graph[current_node].items():

            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(priority_queue,[adjacent,distance])

    return distances

def solution(n, edge):
    answer = 0

    graph = dict()
    #노드의 갯수만큼 미리 할당
    for i in range(n):
        graph[i+1] = dict()

    #엣지 정보로 dict형태의 그래프 만들기
    for i in edge:
        #시작노드 도착노드를 언패킹
        start_node, end_node = i

        #가중치 정보를 전부 1로 해서 간선의 정보 저장
        graph[start_node][end_node] = 1

        #무방향 그래프이므로 반대의 경우도 추가해줌
        graph[end_node][start_node] = 1
    
    #다익스트라로 1번노드로 부터 다른 모든 노드의 최단거리 구하기
    path_info = dijkstra(1,graph)
    
    #간선 갯수가 제일많은 노드를 세기 위해 (key,value)형식으로 변형
    temp = list(path_info.items())

    #value기준으로 정렬
    temp = sorted(temp, key=lambda x: x[1], reverse=True)

    #최대간선의 수는 역순으로 정렬했을때 첫번째 경로정보의 두번째 값
    max_edge = temp[0][1]

    #반복문을 돌면서 max_edge의 값인것들 찾기
    for node,distance in temp:
        if distance == max_edge:
            answer += 1

        #max_edge가 아닌값이 나오면 반복문 빠져나가기 - 정렬해둔상태라 max_edge가 아니면 이것보다 작은 값이라는 의미
        else:
            break

    return answer


'''bfs를 이용한 훨씬빠른 플이'''
from collections import deque


def bfs(start_node, graph):

    count = 0

    visited = dict()

    need_visited = deque(list())

    need_visited.append([start_node,count])

    while need_visited:
        current_node, current_count = need_visited.popleft()

        if current_node not in visited:

            visited[current_node] = current_count

            #다음에 탐색할수 있도록 방문이 필요한 큐에 넣음
            for i in graph[current_node]:

                need_visited.append([i,current_count+1])

        #방문한적있는 노드라면 count값을 비교
        elif visited[current_node] > current_count:

            visited[current_node] = current_count

            for i in graph[current_node]:

                need_visited.append([i,current_count+1])
    
    return visited.items()  


#bfs를 이용한 좀 더 빠른 풀이
def solution2(n, edge):
    answer = 0

    graph = dict()
    #노드의 갯수만큼 미리 할당
    for i in range(n):
        graph[i+1] = list()

    #엣지 정보로 dict형태의 그래프 만들기
    for i in edge:
        #시작노드 도착노드를 언패킹
        start_node, end_node = i

        #가중치 정보를 전부 1로 해서 간선의 정보 저장
        graph[start_node].append(end_node)

        #무방향 그래프이므로 반대의 경우도 추가해줌
        graph[end_node].append(start_node)
    
    temp = list(bfs(1,graph))

    max_path = temp[-1][1]


    for i in reversed(temp):
        if i[1] == max_path:
            answer += 1

        else:
            break

    return answer



if __name__ == "__main__":
    n = 6
    edge = [[3,6],[4,3],[3,2],[1,3],[1,2],[2,4],[5,2]]

    print(solution2(n,edge))
    # assert solution(n,edge) == 3