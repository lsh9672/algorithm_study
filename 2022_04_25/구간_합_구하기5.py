#백준 11660번(누적합, 실버1)
'''
import sys

n,m = map(int,sys.stdin.readline().split())

origin_graph = list()

for _ in range(n):
    origin_graph.append(list(map(int,sys.stdin.readline().split())))

##누적합 표 만들기 - 행
for i in range(n):
    for j in range(1,n):
        origin_graph[i][j] += origin_graph[i][j-1]

total_result = list()

for _ in range(m):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())

    result = 0 

    for i in range(x1-1,x2):
        if y1-1 == 0:
            result += origin_graph[i][y2-1]
        else:
            # print(f"test--------------{(origin_graph[i][y2-1]- origin_graph[i][y1-2])}")
            # print(f"test2-------{origin_graph[i][y2-1]},  {origin_graph[i][y1-2]}")
            result += (origin_graph[i][y2-1]- origin_graph[i][y1-2])

    # print(result)
    total_result.append(result)

for i in total_result:
    print(i)
'''

'''더 빠른 풀이
행만 더하지말고 행 더한후에 세로도 더해서 계산해준다.
'''

import sys

n,m = map(int,sys.stdin.readline().split())

origin_graph = [[0 for _ in range(n+1)]]

for _ in range(n):
    temp = [0] + list(map(int,sys.stdin.readline().split()))
    origin_graph.append(temp)

##누적합 표 만들기 - 행
for i in range(1,n+1):
    for j in range(1,n+1):
        origin_graph[i][j] += origin_graph[i][j-1]

##눅적합 표 만들기 - 열
for i in range(1,n+1):
    for j in range(1,n+1):
        origin_graph[j][i] += origin_graph[j-1][i] 


total_result = list()

for _ in range(m):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())

    result = 0 

    result = (origin_graph[x2][y2] - origin_graph[x2][y1-1]- origin_graph[x1-1][y2] + origin_graph[x1-1][y1-1])

    # print(result)
    total_result.append(result)

for i in total_result:
    print(i)