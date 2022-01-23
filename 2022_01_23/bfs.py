#bfs구현 - 파이썬에서 큐로만 쓰이면(인덱스로 랜덤엑세스없이 Pop,push연산만 한다면)deque를 쓰는게 좋음
from collections import deque


def bfs(start_node:str,graph:dict) -> list:
    #방문한 노드
    # visited = deque(list())

    #방문한 노드를 큐로하면 in연산을 할때 O(n)가 걸린다.
    #따라서 딕셔너리로 구현하는것이 좋다
    visited = dict()

    #방문해야될 노드 
    need_visited = deque(list())

    #첫번째 노드 넣기
    need_visited.append(start_node)

    #반복 - 방문이 필요한 노드가 없을떄까지
    while need_visited:

        #방문할 노드꺼내기
        visit_node = need_visited.popleft()

        #방문여부 확인
        #방문을 안했다면 방문노드 리스트에 추가하고, 방문해야될 노드에 자식노드들 추가
        if visit_node not in visited:
            visited[visit_node] = True
            need_visited.extend(graph[visit_node])
        

    return list(visited.keys())
            

if __name__ == "__main__":
    #그래프 생성
    graph = dict()

    graph['A'] = ['B','C']
    graph['B'] = ['A','D']
    graph['C'] = ['A','G','H','I']
    graph['D'] = ['B','E','F']
    graph['E'] = ['D']
    graph['F'] = ['D']
    graph['G'] = ['C']
    graph['H'] = ['C']
    graph['I'] = ['C','J']
    graph['J'] = ['I'] 

    print(bfs('A',graph))
    assert bfs('A',graph) == ['A','B','C','D','G','H','I','E','F','J']
    
