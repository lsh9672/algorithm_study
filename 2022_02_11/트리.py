#백준 알고리즘 트리 - 1068(그래프, 골드5)

'''아이디어 - 틀린방법(왜틀렸는지 모르겠음)'''
#1. 주어진 입력을 이용해서 트리를 만든다 - 딕셔너리로 만듦
#2. 삭제할 번호로 트리에 접근해서 해당 노드와 자식노드를 전부 지운다.
#3. 최종적으로 만들어진 트리를 반환한다.
#4. 반환된 트리에서 자식노드가 없는 노드번호를 출력한다.
'''
import sys


#트리의 노드개수
n = int(sys.stdin.readline())

#노드의 부모를 입력받음
parent_node_list = list(map(int,sys.stdin.readline().split()))

#삭제할 노드번호
remove_node = int(sys.stdin.readline())

#트리 껍데기 만들기
graph = {node:list() for node in range(n)}

#트리 구성하기
for i in range(len(parent_node_list)):
    #-1이면 루트
    if parent_node_list[i] == -1:
        graph[i] = list()
    
    #부모가 있으면 부모의 위치에 append
    else:
        graph[parent_node_list[i]].append(i)

#노드 삭제
#1. 그래프 딕셔너리(트리)에서 해당 노드를 key로해서 value에 접근한다.
#2. value(자식노드가 저장됨)에 있는 노드들을 찾아서 그래프에서 지워준다.
#3. 재귀를 이용해서 자식의 자식노드들까지 삭제해준다.
child_node_list = graph[remove_node]

#노드를 삭제하는 재귀함수 
def child_remove(child_node):

    #자식노드가 비어있지 않으면 재귀호출
    while graph[child_node] != []:
        #자식노드를 하나씩 꺼내서 재귀함수를 호출한다.
        node = graph[child_node].pop()
        child_remove(node)

    #자식노드가 비어있으면 삭제하고 재귀호출 멈춤
    if graph[child_node] == []:
        #노드삭제
        del graph[child_node]
        return

#재귀함수에 삭제할 노드
child_remove(remove_node)

#부모가 있다면 삭제노드의 부모에 가서 자기 자신 삭제
if parent_node_list[remove_node] != -1:
    graph[parent_node_list[remove_node]].remove(remove_node)


#리프노드 카운트- 딕셔너리의 키들을 다 돌면서 value가 빈 리스트이면 count+1
#초기값 0
count = 0
#그래프의 key 값들로 반복문을 돌림
for i in graph.keys():
    #해당 key의 value가 빈 리스트이면 자식노드가 없다는 뜻, +1함
    if graph[i] == []:
        count+=1

print(count)
'''

'''새로운 접근'''
#1.dfs를 이용해서 접근해보려고 한다.
#2.dfs는 인접노드를 전부 탐색하면서 한 레벨씩 내려가는 것이 아닌 하나의 노드에서 자식노드를 선택해서 탐색하는 방식이다.
#3.dfs로 노드를 탐색하면서 부모노드 정보가 있는 리스트에서 삭제할 노드이면 하위 노드들까지 전부 -2로 바꿔준다(루트랑 안겹치기위헤서)
#4. 그렇게 해서 나온 부모노드 정보 리스트 인덱스를 처음부터 끝까지 탐색하면서 해당인덱스를 부모노드로 쓰는 노드가 없으면 리프노드이다.

import sys


'''입력'''
#트리의 노드개수
n = int(sys.stdin.readline())

#노드의 부모를 입력받음
parent_node_list = list(map(int,sys.stdin.readline().split()))

#삭제할 노드번호
remove_node = int(sys.stdin.readline())


#돌면서 삭제할 노드들을 전부 -2로 바꿔준다.
def dfs(remove_node,parent_node_list):

    #삭제할 노드를 -2로 표시해준다.
    parent_node_list[remove_node] = -2

    #삭제할 노드의 자식노드들을 dfs로 탐색하면서 전부 바꿔준다.
    #반복문을 돌면서 삭제노드를 부모로 사용하는 노드가 있으면 그 값을 remove_node로 해서 재귀호출한다.
    for i in range(len(parent_node_list)):
        if remove_node == parent_node_list[i]:
            dfs(i,parent_node_list)

#dfs탐색이 끝나면 삭제노드와 그 자식노드들은 전부 -2로 표시가 되어있을것이다.
dfs(remove_node,parent_node_list)

#반복문을 돌면서 리프노드의 개수를 세준다.
#리프노드는 parent_node_list에서 -2가 아니고, parent_node_list안에 없는 값이어야 한다.(없어야 해당노드가 부모로 쓰이지 않았다는 뜻 즉, 리프 노드다)
count = 0

for i in range(len(parent_node_list)):
    if i not in parent_node_list and parent_node_list[i] !=-2:
        count+=1

print(count)
