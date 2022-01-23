#dfs 구현


def dfs(start_node:str,graph:dict)->list:
    #방문한 노드 - 큐
    # visited = list()

    #딕셔너리로 방문노드 구하는게 좀더 효율적
    visited = dict()

    #방문이 필요한 노드 - 스택
    need_visited = list()

    #시작노드 넣기
    need_visited.append(start_node)

    #방문이 필요한 노드가 없을때 까지 반복
    while need_visited:

        visit_node = need_visited.pop()

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

    print(dfs('A',graph))

    assert dfs('A',graph) == ["A","C","I","J","H","G","B","D","F","E"]
