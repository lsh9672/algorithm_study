#백준 2458번 (그래프,골드4)
import sys

n,m = map(int,sys.stdin.readline().split())

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())

    graph[a][b] = 1

for k in range(1, n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][k] == graph[k][j] == 1:
                graph[i][j] = 1

result = 0

for i in range(n+1):
    temp = 0
    for j in range(n+1):
        temp += graph[i][j] + graph[j][i]

    if temp == n-1:
        result += 1

print(result)