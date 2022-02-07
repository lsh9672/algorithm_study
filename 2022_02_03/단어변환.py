#프로그래머스 level 3 단어변환(dfs/bfs)

'''아이디어 -처음 아이디어'''
#1 각 단어를 노드로 생각한다(start노드는 begin안에 있는 변수)
#2 인접노드는 한글자만 바뀌고 words안에 있는 단어로 구성한다.
#3 한글자 차이의 확인은 별도의 함수(check)를 통해서 판단하도록 한다
#4 begin을 시작노드로 하고, words의 단어로 트리를 생성한다.
#5 bfs로 탐색하면서 노드 탐색시마다 가중치를 1씩더해서 최소 몇번만에 도달했는지 확인한다
#6 방문노드 확인을 dict로 만들어서 value에 거친 단계의 최소값을 저장한다
#7 최종적으로 방문확인 dict를 반환하고 target노드의 값을 출력한다.

from collections import deque


#단어차이가 1인 것을 판별하는 함수
def check(node,word:str)-> bool:
    count= 0

    for i in range(len(node)):
        if node[i] != word[i]:
            count+=1
        
        if count >=2:
            return False
    if count == 1:

        return True
    else:
        return False

#만들어진 트리를 탐색하는 함수
def bfs(start_node:str,graph:dict)-> dict:

    visited = dict()

    need_visited = deque(list())

    #탐색을 위해 처음 값 넣기
    need_visited.append([start_node,0])

    #반복하면서 탐색
    while need_visited:
        current_node,current_count = need_visited.popleft()

        if current_node not in visited:
            visited[current_node] = current_count
            
            if current_node in graph:
                for i in graph[current_node]:
                    need_visited.append([i,current_count+1])

        elif current_node in visited and visited[current_node] > current_count:
            visited[current_node] = current_count
            
    return visited

#실제로 돌아가는 로직
def solution(begin, target, words):
    answer = 0

    #target단어가 words안에 없다면
    if target not in words:
        return 0 

    #그래프형태로 만들기 - dict형태로 만듦
    temp = [begin] + words
    graph = {node:list() for node in temp}

    temp_queue = deque(temp)

    for i in temp:
        for j in temp:

            if check(i,j) == True:
                graph[i].append(j)

    result = bfs(begin,graph)

    return result[target]


'''두번째 아이디어'''
#위의 첫번째 풀이는 그래프로 생각하고 그래프를 미리 만들어야되서 시간이 오래걸린다
#따라서 그래프를 미리 만들지 않고 bfs탐색시에 만들면서 탐색하는 방법을 고민해보았다.
#문자 체크 함수는 그대로 썼다
#bfs2함수의 인자에는 그래프 대신 words리스트가 들어올것이다
#탐색이 필요한 노드에 주어진 `begin` 단어와 count=0 이 들어갈것이다
#word를 반복문으로 돌면서 자식노드로서 조건에 부합하는 값이 있으면 방문표시를 True로 하고 다음 탐색을 위해 need_visited에 넣는다.
#need_visted에서 하나씩 꺼내면서 탐색하다가, target을 만나면 해당 노드에 저장된 count값을 출력한다.
#훨씬 빠르다 - 노드가 늘어날수록 더 빠를것이다.


def bfs2(start_node,target,graph) -> int:

    visited = [False for _ in range(len(graph))]
    count = 0

    need_visited = deque(list())
    need_visited.append([start_node,0])

    while need_visited:
        current_node,current_count = need_visited.popleft()

        #만약 target단어면 current_count를 return
        if current_node == target:
            count = current_count
            break

        
        for i in range(len(graph)):
            if check(current_node,graph[i]) == True:

                if visited[i] == False:
                    visited[i] = True
                    need_visited.append([graph[i],current_count+1])


    return count 

def solution2(begin, target, words):

    #target단어가 words안에 없다면
    if target not in words:
        return 0 

    result = bfs2(begin,target,words)

    return result

if __name__ == "__main__":

    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    # solution(begin,target,words)
    assert solution2(begin,target,words) == 4

    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log"]
    assert solution2(begin,target,words) == 0
