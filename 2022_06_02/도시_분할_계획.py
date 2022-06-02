#백준 1647번 (mst, 골드4)

import sys

n,m = map(int,sys.stdin.readline().split())

edge_list = list()

for _ in range(m):
    temp = list(map(int,sys.stdin.readline().split()))

    edge_list.append(temp)

edge_list.sort(key=lambda x : x[2])

parent_list = [i for i in range(n+1)]

def find_func(node):

    while parent_list[node] != node:
        node = parent_list[node]

    return node

def union_func(a,b):

    a = find_func(a)
    b = find_func(b)

    if a < b:
        parent_list[b] = a
    else:
        parent_list[a] = b


temp_edge_list = list()

for a,b,weight in edge_list:

    if find_func(a) != find_func(b):

        union_func(a,b)

        temp_edge_list.append(weight)

        if len(temp_edge_list) == n-1:
            break

print(sum(temp_edge_list) - max(temp_edge_list))