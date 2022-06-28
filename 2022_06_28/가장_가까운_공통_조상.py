#백준 3584번 (골드4, 트리)
import sys

test_case = int(sys.stdin.readline().strip())

for _ in range(test_case):
    node_num = int(sys.stdin.readline().strip())
    
    ## 인덱스가 노드, 값이 부모노드
    parent_list = [i for i in range(node_num+1)]

    for _ in range(node_num-1):
        a,b = map(int,sys.stdin.readline().split())

        parent_list[b] = a

    first_node, second_node = map(int,sys.stdin.readline().split())

    first_parent_list = [first_node]
    second_parent_list = [second_node]

    while parent_list[first_node] != first_node:
        first_parent_list.append(parent_list[first_node])
        first_node = parent_list[first_node]

    while parent_list[second_node] != second_node:
        second_parent_list.append(parent_list[second_node])
        second_node = parent_list[second_node]


    result = -1

    while (len(first_parent_list) != 0 and len(second_parent_list) != 0) and first_parent_list[-1] == second_parent_list[-1]:
        result = first_parent_list[-1]
        first_parent_list.pop()
        second_parent_list.pop()

    print(f"final result : {result}")

