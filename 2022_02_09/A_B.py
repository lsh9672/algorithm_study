#백준알고리즘 16953 - A->B (실버1, 그래프)

'''아이디어'''
#1. 각 숫자를 노드로 생각하고, 인접한노드를 2를 곱했을때, 1을 수의 오른쪽에 추가했을떄, 두가지로 볼수있다.
#2. 이렇게 그래프로 보게 되면, bfs로 탐색을 할수 있다.
#3. 각 노드마다 탐색시에 몇번 연산을 했는지를 저장한다.
#4. B에 도달했으면 연산횟수를 반환해준다.
#5. 이때 다음노드로 선정할 수는 10^9으로 제한한다.(제한하지 않으면 너무 많아져서 메모리초과가 된다.)

#필요한 모듈 : sys => 입출력, deque : bfs탐색에 필요한 큐
import sys
from collections import deque

'''재귀풀이 - 시간초과
a,b = sys.stdin.readline().split()

#함수 정의
def test(a:str,b:str):
    if int(a) == int(b):
        return 1

    elif int(a) < int(b):
        #끝자리가 1이면
        if b[-1] == '1':
            if test(a,b[:-1]) == -1:
                return -1
            return test(a,b[:-1])+1
        #끝자리가 1이 아니면
        elif int(b) % 2 == 0:
            if test(a,str(int(b)//2)) == -1:
                return -1
            return test(a,str(int(b)//2)) + 1
        else:
            return -1
            
    elif int(a) > int(b):
        return -1

print(test(a,b))

'''

'''입력'''
a,b = sys.stdin.readline().split()

#메모리 초과가 안나도록
max = 10**9

#bfs정의
def bfs(start_node:str,end_node:str):

    visited = dict()

    need_visited = deque(list())

    need_visited.append([start_node,1])

    visited[start_node] = 1

    while need_visited:

        current_node, current_count = need_visited.popleft()

        if current_node == end_node:
            return current_count
        
        next_node_list = [str(int(current_node)*2),current_node+'1']

        for next_node in next_node_list:

            if next_node not in visited and int(next_node) <= max:
                visited[next_node] = current_count + 1
                need_visited.append([next_node,current_count+1])

    return -1

print(bfs(a,b))

