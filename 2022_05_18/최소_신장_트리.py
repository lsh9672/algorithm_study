#백준 1197번 (그래프, 골드4)

'''
크루스칼을 이용한 풀이

아래의 풀이는 매번 대표노드를 찾기 위해 반복문을 돌리기 때문에 느림
따라서 유니온 과정에서 전부 업데이트를 해야됨



import sys


v,e = map(int,sys.stdin.readline().split())

edge_list = list()

for _ in range(e):
    temp = list(map(int,sys.stdin.readline().split()))
    edge_list.append(temp)

##간선가중치를 오름차순으로 정렬

edge_list.sort(key=lambda x : x[2])

##부모노드를 가르키는 리스트
parent_node_list = [i for i in range(v)]

##루트노드 찾는 함수
def find_func(node):

    while node != parent_node_list[node]:
        node = parent_node_list[node]
    return node

weight_count = 0

##간선을 찾을때마다 카운트하고 노드수-1이 되면 모든 노드가 연결된것
edge_count = 0

##간선의 가중치가 낮은 순서대로 하나씩 간선을 뽑고, 싸이클이 생기는지 확인함.

for a,b,weight in edge_list:
    ## 대표노드 즉, 대표하는 루트노드를 찾았을때, 같지 않으면 사이클이 안생긴것
    a = a-1
    b = b-1 
    if find_func(a) != find_func(b):
        ##서로 최대부모노드가 다르면 union작업을 함
        parent_node_list[find_func(b)] = find_func(a)
        ##사이클이 안생겼으면 가중치 저장
        weight_count += weight

        edge_count+=1

        ##누적한 간선수가 노드-1이면 다 연결된 것
        if edge_count == v-1:
            break
print(weight_count)
'''

'''
부모노드를 가르키는 리스트를 업데이트 하는 유니온 함수추가
'''
import sys


v,e = map(int,sys.stdin.readline().split())

edge_list = list()

for _ in range(e):
    temp = list(map(int,sys.stdin.readline().split()))
    edge_list.append(temp)

##간선가중치를 오름차순으로 정렬

edge_list.sort(key=lambda x : x[2])

##부모노드를 가르키는 리스트
parent_node_list = [i for i in range(v)]

##루트노드 찾는 함수
def find_func(node):

    while node != parent_node_list[node]:
        node = parent_node_list[node]
    return node

def union_func(a,b):
    a = find_func(a)
    b = find_func(b)

    if a < b:
        parent_node_list[b] = a
    else:
        parent_node_list[a] = b

weight_count = 0

##간선을 찾을때마다 카운트하고 노드수-1이 되면 모든 노드가 연결된것
edge_count = 0

##간선의 가중치가 낮은 순서대로 하나씩 간선을 뽑고, 싸이클이 생기는지 확인함.

for a,b,weight in edge_list:
    ## 대표노드 즉, 대표하는 루트노드를 찾았을때, 같지 않으면 사이클이 안생긴것
    a = a-1
    b = b-1 
    if find_func(a) != find_func(b):
        ##서로 최대부모노드가 다르면 union작업을 함
        union_func(a,b)
        ##사이클이 안생겼으면 가중치 저장
        weight_count += weight

        edge_count+=1

        ##누적한 간선수가 노드-1이면 다 연결된 것
        if edge_count == v-1:
            break
print(weight_count)





