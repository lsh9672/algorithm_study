#백준 16398번 (최소 스패닝 트리)
import sys

n = int(sys.stdin.readline().strip())

temp_input= [[0 for _ in range(n+1)]]

for _ in range(n):
    temp_input.append([0] + list(map(int,sys.stdin.readline().split())))


edge_list = list()

for i in range(1,n+1):
    for j in range(1,n+1):
        if i!=j:
            edge_list.append([i,j,temp_input[i][j]])

edge_list.sort(key=lambda x : x[2])

parent_list = [i for i in range(n+1)]

def find_func(node):

    while node != parent_list[node]:
        node = parent_list[node]

    return node

def union_func(node1,node2):

    node1 = find_func(node1)
    node2 = find_func(node2)


    if node1 < node2:
        parent_list[node2] = node1
    
    else:
        parent_list[node1] = node2

edge_count = 0


result = 0

for a,b,weight in edge_list:

    if find_func(a) != find_func(b):
        union_func(a,b)

        edge_count += 1

        result += weight

        if edge_count == n-1:
            break

print(result)