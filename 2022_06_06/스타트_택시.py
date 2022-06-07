#백준 19238번 (시뮬레이션, 골드3)
import sys
# from collections import deque


n,m,fuel_num = map(int,sys.stdin.readline().split())

field = list()


for _ in range(n):
    field.append(list(map(int,sys.stdin.readline().split())))

start_node = list(map(int,sys.stdin.readline().split()))

passenger_start_end = dict()


##승객의 위치는 2로 표시
for _ in range(m):
    start_x,start_y,end_x,end_y = map(int,sys.stdin.readline().split())

    field[start_x-1][start_y-1] = 2

    passenger_start_end[(start_x-1,start_y-1)] = [end_x-1,end_y-1]
##상,하,좌,우
dx = [-1,1,0,0]
dy = [0,0,-1,1]


## end_node == [-1,-1] 이면 승객 태우러 가는것
## end_node != [-1,-1] 아니면 승객태우고 목적지로 가는것
def bfs(start_node:list,graph:list,end_node:list):
    global fuel_num

    visited = [[0 for _ in range(n)] for _ in range(n)]

    need_visited = list()

    need_visited.append(start_node+[0])

    visited[start_node[0]][start_node[1]] = 1


    while need_visited:

        need_visited.sort(key=lambda x : (x[2],x[0],x[1]))

        current_x,current_y,current_weight = need_visited.pop(0)

        ##승객한테 가는 경우
        if end_node[0] == -1 and end_node[0] == -1:
            
            ## 연료가 바닥난 경우
            if current_weight >= fuel_num:
                return -1
            
            ## 바닥나지 않았다면 승객위치인지 아닌지 확인해야됨
            else:
                ## 승객이라면
                if graph[current_x][current_y] == 2:
                    fuel_num -= current_weight
                    graph[current_x][current_y] = 0
                    return (current_x,current_y)

                else:
                    for i in range(4):
                        next_x = current_x + dx[i]
                        next_y = current_y + dy[i]

                        if (0 <= next_x < n) and (0 <= next_y < n) and visited[next_x][next_y] == 0 and graph[next_x][next_y] != 1:
                            need_visited.append([next_x,next_y,current_weight+1])
                            visited[next_x][next_y] = 1

        ## 승객을 태우고 목적지로 가는 경우
        else:
            if current_weight > fuel_num:
                # print("--------------1")
                return -1
            elif current_weight == fuel_num:
                # print(f"check location : {current_x},{current_y}")
                if end_node[0] == current_x and end_node[1] == current_y:
                    # print("--------------2")
                    fuel_num -= current_weight
                    return current_weight
                # else:
                #     print("--------------3")
                #     return -1
            else:
                if end_node[0] == current_x and end_node[1] == current_y:
                    # print("--------------4")
                    fuel_num -= current_weight
                    return current_weight
                else:
                    for i in range(4):
                        next_x = current_x + dx[i]
                        next_y = current_y + dy[i]

                        if (0 <= next_x < n) and (0 <= next_y < n) and visited[next_x][next_y] == 0 and graph[next_x][next_y] != 1:
                            need_visited.append([next_x,next_y,current_weight+1])
                            visited[next_x][next_y] = 1
    # print("--------------5")
    return -1

start_node = [start_node[0]-1,start_node[1]-1]

for _ in range(m):

    ## 승객 태우러감
    go_to_passenger = bfs(start_node,field,[-1,-1])
    print(f"go_to_passenger : {go_to_passenger}")

    if go_to_passenger == -1:
        fuel_num = -1
        break
    else:
        start_node = [go_to_passenger[0],go_to_passenger[1]]
    
    go_to_destination = bfs(start_node,field,passenger_start_end[go_to_passenger])
    print(f"go_to_destination : {go_to_destination}")

    if go_to_destination == -1:
        fuel_num = -1
        break
    else:
        start_node = passenger_start_end[go_to_passenger]
        fuel_num += go_to_destination * 2

print(fuel_num)