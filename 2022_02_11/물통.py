#백준 - 물통(2251번,실버1, 그래프) 

'''아이디어 - 실패한'''
#1. ABC 세 물통의 상태를 묶어서 노드로 생각하고, 인접 노드를 다른 물통에 물을 부어서 변한 상태라고 보면 그래프로 생각할수가 있다.
#2. 그래프로 봤기 때문에 bfs/dfs/ 탐색방법을 이용해서 원하는 노드를 찾을수 있다.
#3. 물을 옮길수 있는 경우의 수는 A->B,A->C, B->A,B->C, C->A,C->B로 6가지가 나온다. 
#4. 또한 문제에서 물을 부을때 다 비워질때까지 쏟아붓는 경우, 또는 대상 물통이 꽉찰때까지 붓는 경우 두가지라고 했다.
#5. 따라서 4번의 규칙을 지키면서(물통이 넘치지 않게 하면서) 3번의 경우의 수롤 전부 인접노드로 만들어준다.
#6. 각 상태들을 dict의 key로 두어서 중복을 방지한다.(방문 처리)
#7. 또한 C의 값을 저장할 dict형을 하나 더 두어서 저장한다.

'''아이디어 - 성공'''
# 기존의 아이디어는 A,B,C 3개를 저장했는데, 그럴필요없이 a,b만 저장하면 전체에서 a+b값을 빼면된다.
# 노드를 a,b로 저장하는 식으로 다시 해본다.


import sys
from collections import deque


'''입력'''
a,b,c = map(int,sys.stdin.readline().split())

#시작노드 만들기 - 시작은 0,0이 비어있음
start_node = (0,0)

#방문처리츨 할 딕셔너리
visited = dict()

#방문확인을 6번씩 해야되므로 따로 함수로 분리 - True면 방문안해서 추가함, False면 이미 방문한 노드
def check(node:tuple) -> bool:

    if node not in visited:
        visited[node] = 1
        return True
    
    else:
        return False


#bfs 함수 정의 - 노드를 딕셔너리에 키로 저장해야되기 때문에 튜플로 한다.,water_count를 반환한다.
def bfs(start_node:tuple,water_total:int) -> set:


    #C의 값 저장 - A가 0일때만 저장, set으로 만들어서 중복데이터저장을 방지
    water_count = set()

    #방문이 필요한 노드를 넣을 큐
    need_visited = deque(list())

    #시작노드를 방문이 필요한 노드에 넣음 - A가 0일떄만 방문처리
    need_visited.append(start_node)

    
    while need_visited:
        print(need_visited)


        #방문해야될 노드를 꺼냄
        current_a,current_b = need_visited.popleft()

        current_c = water_total - (current_a+current_b)

        '''인접노드를 만듦 - 6가지 경우,최대치 생각해줘야됨.'''
        #A->B A->C B->A B->C C->A C->B

        #1. 현재노드의 a가 0이면 c의 값을 저장
        if current_a == 0:
            water_count.add(water_total - (current_a+current_b))
        
        #2. A->B일때
        #물의 양을 체크함 -> 전부 부을수 있는지 없는지
        # b는 입력받은 물통크기 

        #옮길수 있는 물의양
        move_amount_of_water = min(current_a,b-current_b)
        temp_node = (current_a - move_amount_of_water,current_b + move_amount_of_water)
        if check(temp_node) == True:
            need_visited.append(temp_node)
        
        #3. A->C일때
        move_amount_of_water = min(current_a,c - current_c)
        temp_node = (current_a - move_amount_of_water,current_b)
        if check(temp_node) == True:
            need_visited.append(temp_node)
        

        #4. B->A일때
        move_amount_of_water = min(current_b,a-current_a)
        temp_node = (current_a + move_amount_of_water,current_b - move_amount_of_water)
        if check(temp_node) == True:
            need_visited.append(temp_node)

        #5. B->C일때
        move_amount_of_water = min(current_b,c-current_c)
        temp_node = (current_a,current_b - move_amount_of_water)
        if check(temp_node) == True:
            need_visited.append(temp_node)

        #6. C->A일때
        move_amount_of_water = min(current_c,a-current_a)
        temp_node = (current_a + move_amount_of_water,current_b)
        if check(temp_node) == True:
            need_visited.append(temp_node)

        #7. C->B일때
        move_amount_of_water = min(current_c,b-current_b)
        temp_node = (current_a,current_b + move_amount_of_water)
        if check(temp_node) == True:
            need_visited.append(temp_node)

    return water_count

result = sorted(list(bfs(start_node,c)))
print(' '.join(list(map(str,result))))











        
