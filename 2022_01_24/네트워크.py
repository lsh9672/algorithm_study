#프로그래머스 level3 네트워크
from collections import deque


#BFS
def bfs(start_node,graph):
    #방문한 노드 저장
    visited = dict()

    need_visited = deque(list())

    need_visited.append(start_node)

    while need_visited:

        current_node = need_visited.popleft()

        if current_node not in visited:

            visited[current_node] = True

            need_visited.extend(graph[current_node])

    return set(visited.keys())

def solution(n, computers):
    answer = 0
    
    graph = dict()

    #주어진 트리를 이해하기 편한 사전형으로 변환
    for index,value in enumerate(computers):

        graph[str(index+1)] = list()

        for a,b in enumerate(value):

            if b == 1:
                graph[str(index+1)].append(str(a+1))

    temp = graph.keys()

    check_list = set(temp)
    
    while check_list:
        current_node = list(check_list)[0]
        check_list = check_list - bfs(current_node,graph)
        answer += 1

        
    return answer


if __name__ == "__main__":
    
    n = 3
    computers = [[1,1,0],[1,1,0],[0,0,1]]
    assert solution(n,computers) == 2

    n = 3
    computers = [[1,1,0],[1,1,1],[0,1,1]]
    assert solution(n,computers) == 1
