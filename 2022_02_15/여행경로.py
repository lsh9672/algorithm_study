#프로그래머스 bfs/dfs 여행경로

from collections import defaultdict


def dfs(start_node, graph):

    path = list()

    need_visited  = list()

    need_visited.append(start_node)

    while need_visited:
        current_node = need_visited[-1]


        #해당 위치에서 출발하는 티켓이 없던가, 티켓을 다사용한 경우(자식노드가 없는 경우)
        if current_node not in graph or len(graph[current_node]) == 0:
            #경로에 추가
            path.append(need_visited.pop())
    
        
        #다음 위치로 가는 표가 있으면
        else:
            need_visited.append(graph[current_node].pop())

    return path

def solution(tickets):

    #그래프 만들기
    graph = defaultdict(list)

    for i in tickets:
        
        graph[i[0]].append(i[1])

    #알파벳순으로 빠른 값으로 출력하기 위해 자식노드들 정렬
    for j in graph.keys():
        graph[j].sort(reverse=True)

    answer = dfs("ICN",graph)

    #거꾸로 경로를 구했기 때문에 한번 뒤집어주어야됨
    answer.reverse()

    return answer


if __name__ == "__main__":
    tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    assert solution(tickets) == ["ICN", "JFK", "HND", "IAD"]

    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
    assert solution(tickets) == ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]


