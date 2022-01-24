#다익스트라 구현
import heapq


def dijkstra(start_node,graph):

    #A에서 각 노드의 경로를 저장할 배열 생성(초기값은 무한대 - inf 로 잡음)
    distances = {node:float('inf') for node in graph}

    #시작노드의 경우 자기 자신이므로 가중치를 0으로 둠
    distances[start_node] = 0

    #각 노드의 가중치들을 저장해둘 우선순위 큐(힙을 이용하기 때문에 가중치가 작은 값이 위로 올라옴)
    priority_queue = []

    #첫번째 값 넣어두기 - 힙이므로 heapq를 이용해서 넣는다
    heapq.heappush(priority_queue,[start_node,distances[start_node]])

    #반복하면서 최단거리 찾기 - 우선순위 큐가 빌때까지 반복
    while priority_queue:
        #힙에서 하나 꺼내서 변수에 넣기
        current_node,current_distance = heapq.heappop(priority_queue)

        #현재 저장되어 있는 경로의 가중치가 힙에서 뽑은 값보다 작으면 패스
        if distances[current_node] < current_distance:
            continue
        
        #현재노드의 인접한 노드 정보를 빼내서 현재 노드의 거리정보랑 인접노드의 가중치를 더함
        for adjacent,weight in graph[current_node].items():
            #거리 계산
            distance = current_distance +weight

            #저장되어있는 경로와 비교해서 새로운 경로가 더 가중치가 작으면 업데이트
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(priority_queue,[adjacent,distance])

    return distances


if __name__ == "__main__":

    graph = dict()

    graph["A"] = {"B":8,"C":1,"D":2}
    graph["B"] = {}
    graph["C"] = {"B":5,"D":2}
    graph["D"] = {"E":3,"F":5}
    graph["E"] = {"F":1}
    graph["F"] = {"A":5}

    print(dijkstra("A",graph))