#백준 11779번 (다익스트라, 골드4)
import sys
import heapq

INF = float("inf")

n = int(sys.stdin.readline().strip())

m = int(sys.stdin.readline().strip())

graph = [[-1 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a,b,weight = map(int,sys.stdin.readline().split())

    if graph[a][b] == -1 or graph[a][b] > weight:
        graph[a][b] = weight
    

start_node,end_node = map(int,sys.stdin.readline().split())

##다익스트라
def dijkstra(start_node,end_node):

    distance = [INF for _ in range(n+1)]

    path = [i for i in range(n+1)]

    queue = list()
    distance[start_node] = 0

    heapq.heappush(queue,[distance[start_node],start_node])

    while queue:
        current_weight,current_node = heapq.heappop(queue)

        if distance[current_node] < current_weight:
            continue

        for next_node,temp_weight in enumerate(graph[current_node]):
            if temp_weight == -1:
                continue
            next_weight = temp_weight + current_weight
            if distance[next_node] > next_weight:
                distance[next_node] = next_weight

                path[next_node] = current_node
                heapq.heappush(queue,[next_weight,next_node])
    
    
    
    ##경로 구하기
    result_path = [end_node]

    result = str(distance[end_node]) + "\n"
    
    while path[end_node] != end_node:
        result_path.append(path[end_node])

        end_node = path[end_node]

    result += str(len(result_path)) + "\n" + " ".join(list(map(str,result_path[::-1])))


    return result

print(dijkstra(start_node,end_node))
