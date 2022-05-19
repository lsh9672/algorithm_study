#백준 4195번(자료구조, 골드2)
import sys


test_case = int(sys.stdin.readline().strip())

## 두 그래프를 합치는 함수
def union_func(first,second):

    first_root = find_func(first)
    second_root = find_func(second)

    if first_root != second_root:
        parent[second_root] = first_root
        count[first_root] += count[second_root]
    
##루트노드를 찾아주는 함수
def find_func(first):

    if parent[first] == first:
        return first

    else:
        root_node = find_func(parent[first])
        parent[first] = root_node
        return parent[first]


for _ in range(test_case):

    parent = dict()
    count = dict()

    f = int(sys.stdin.readline().strip())

    for _ in range(f):
        first_friend, second_friend = sys.stdin.readline().split()

        if first_friend not in parent:
            parent[first_friend] = first_friend
            count[first_friend] = 1

        if second_friend not in parent:
            parent[second_friend] = second_friend
            count[second_friend] = 1

        
        union_func(first_friend,second_friend)

        print(count[find_func(first_friend)])



