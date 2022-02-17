#프로그래머스 - 순위 (그래프, 레벨3)
'''아이디어'''
#주어진 경기결과와 n을 이용해서 그래프를 만든다.
#1번부터 각각 탐색을 돈다
#경기 결과를 보면서 자신이 이긴선수 리스트, 진선수 리스트를 만든다.
#자신의 등수를 계산한다.

def dfs(start_node, graph):

    #스타트 노드가 이긴 놈들
    win_list = list()

    need_visited = [start_node]


    while need_visited:
        current_node = need_visited.pop()

        for i in graph[start_node]:
            if i not in win_list:
                win_list.append(i)
                need_visited.append(i)
    
    return win_list

def solution(n, results):
    answer = 0

    #그래프 - 0번은 안씀
    graph = [list() for j in range(n+1)]


    for i in results:
        graph[i[0]].append(i[1])

    #내가 이긴놈들 리스트
    win_list = [0]*(n+1)
    for j in range(1,n+1):
        win_list[j] = set(dfs(j,graph))
    
    #이긴놈들 리스트 업데이트
    for x in range(1,n+1):
        for y in list(win_list[x]):
            win_list[x].update(win_list[y])

    #나를 이긴놈들 리스트
    lose_list = [list() for i in range(n+1)]
    for x in range(1,n+1):
        for y in list(win_list[x]):
            lose_list[y].append(x)
    print(f"win: {win_list}")
    print(f"lose: {lose_list}")
    #계산 - 나를 이긴놈들 리스트와, 내가 이긴놈들 리스트의 길이를 합쳤을떄, n-1(자기자신을 제외)이면 순위을 알수있음
    for i in range(1,n+1):
        if len(win_list[i])+len(lose_list[i]) == n-1:
            answer+=1

    return answer


if __name__ == "__main__":
    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    # assert solution(n,results) == 2

    n = 5
    results = [[1, 2], [4, 5], [3, 4], [2, 3]]
    
    print(solution(n,results))
    # assert solution(n,results) == 5