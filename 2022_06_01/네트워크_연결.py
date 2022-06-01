#백준 1922번 (mst, 골드4)

## 크루스칼을 이용해서 해결
import sys

n = int(sys.stdin.readline().strip())

m = int(sys.stdin.readline().strip())

## 엣지의 가중치를 저장하고 정렬할 리스트
edge_list = list()

for _ in range(m):
    temp = list(map(int,sys.stdin.readline().split()))
    edge_list.append(temp)

edge_list.sort(key = lambda x: x[2])

##최대부모를 저장할 리스트
parent_list = [i for i in range(n+1)]

##최소비용을 저장할 변수
result = 0

##간선수가 노드-1이면 모든 노드가 이어졌다는 뜻
edge_count = 0

## 크루스칼 로직

##최대 부모를 찾는 함수
def find_parent(node):
    
    while parent_list[node] != node:

        node = parent_list[node]
    
    return node

## 두 그래프를 합치는 함수
def union_function(a,b):
    node1 = find_parent(a)
    node2 = find_parent(b)

    if node1 < node2:
        parent_list[node2] = node1
    else:
        parent_list[node1] = node2


for a,b,weight in edge_list:

    ## 두 노드의 부모를 찾고 다르면 합치는 작업을 함
    if find_parent(a) != find_parent(b):
        union_function(a,b)

        result += weight

        edge_count += 1

        if edge_count == n-1:
            break

print(result)