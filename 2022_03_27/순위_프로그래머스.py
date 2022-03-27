#프로그래머스 레벨3 - 순위 (수정)
def solution(n, results):
    answer = 0


    graph = [[0 for _ in range(n)] for _ in range(n)]
    #1이면 이김, -1이면 짐
    for a,b in results:
        graph[a-1][b-1] = 1
        graph[b-1][a-1] = -1

    for k in range(n):
        for i in range(n):
            for j in range(n):

                #이미 확인된 결과이면,
                if i == j or graph[i][j] != 0:
                    continue

                if graph[i][k] == graph[k][j] == 1:
                    graph[i][j] = 1

                    graph[j][i] = -1
                    graph[k][i] = -1
                    graph[j][k] = -1

    #0이 1개만 있으면 순위를 알수 있음(0은 자기 자신)
    for i in graph:
        if i.count(0) == 1:
            answer += 1

    return answer

if __name__ == "__main__":

    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    assert solution(n,results) == 2