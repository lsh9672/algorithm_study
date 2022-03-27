#백준 16932번 (그래프 연습, 골드4)
'''틀린 풀이 - 완탐이다, 0인 부분에 1을 하나씩 놓고 탐색해서 가장 큰 값을 출력한다, 하지만 시간초과가 난다.
import sys
from collections import deque

n,m  = map(int,sys.stdin.readline().split())

graph = list()

zero_list = list()

for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    graph.append(temp)
    for j in range(m):
        if temp[j] == 0:
            zero_list.append([i,j])

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(start_node:list,visited:list)-> int:

    need_visited = deque(list())
    need_visited.append(start_node)

    count = 0

    while need_visited:

        current_x,current_y = need_visited.popleft()

        count+=1

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if (0 <= next_x < n) and (0 <= next_y < m) and graph[next_x][next_y] == 1 and visited[next_x][next_y] == 0:
                visited[next_x][next_y] = 1
                need_visited.append([next_x,next_y])
    
    return count


max_value = -1
#0으로 되어있는 것중에 하나를 변경
for x,y in zero_list:

    #주위에 1이 없으면 패스
    check = False
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if (0<= next_x < n) and (0 <= next_y < m):
            if graph[next_x][next_y] == 1:
                check=True
                break
        
    if check == False:
        continue

    graph[x][y] = 1

    visited = [[0 for _ in range(m)] for _ in range(n)]

    visited[x][y] = 1

    max_value = max(max_value,bfs([x,y],visited))

    graph[x][y] = 0

print(max_value)
'''


import sys
from collections import deque

n,m  = map(int,sys.stdin.readline().split())

graph = list()

zero_list = list()

for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    graph.append(temp)
    for j in range(m):
        if temp[j] == 0:
            zero_list.append([i,j])

visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(start_node:list,group_num:int)-> int:

    need_visited = deque(list())
    need_visited.append(start_node)

    count = 0

    while need_visited:

        current_x,current_y = need_visited.popleft()

        count+=1

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if (0 <= next_x < n) and (0 <= next_y < m) and graph[next_x][next_y] == 1 and visited[next_x][next_y] == 0:
                visited[next_x][next_y] = group_num
                need_visited.append([next_x,next_y])
    
    return count


#bfs함수를 돌리면서 group num을 업데이트 시켜둠
group_num = 1
group_dict = dict()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = group_num
            group_dict[group_num] = bfs([i,j],group_num)
            group_num += 1

result = 0
for x,y in zero_list:

    temp = set()

    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if (0 <= next_x < n) and (0 <= next_y < m):
            if graph[next_x][next_y] == 1 and visited[next_x][next_y] not in temp:
                temp.add(visited[next_x][next_y]) 

    
    temp_count = 1 
    for z in temp:
        temp_count += group_dict[z]

    result = max(temp_count, result)

print(result)