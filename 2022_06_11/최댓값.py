## 백준 2566
import sys

graph = list()

for _ in range(9):
    graph.append(list(map(int,sys.stdin.readline().split())))

max_value = -1
result =""

for i in range(9):
    for j in range(9):
        if max_value < graph[i][j]:
            max_value = graph[i][j]
            result = f"{i+1} {j+1}"

print(max_value)
print(result)