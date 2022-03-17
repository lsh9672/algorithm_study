#백준 21610번 (마법사 상어와 비바라기, 시뮬레이션 골드5)
import sys

'''입력'''
n,m = map(int,sys.stdin.readline().split())

field = list()

#맵 입력받기
for _ in range(n):
    field.append(list(map(int,sys.stdin.readline().split())))


'''명령 처리를 위한 함수들 정의'''
def total_water():
    result = 0

    for i in range(n):
        for j in range(n):
            result += field[i][j]

    return result


cloud_field = [[0 for _ in range(n)] for _ in range(n)]

#구름 위치좌표
cloud_location_list = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]


#이동 방향
move_dir_list = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]

#1번 동작 - 구름이 이동, 구름의 위치를 리스트로 반환.
def cloud_move(dir:int,distance:int,cloud_location:list)->list:

    move_distance_x = move_dir_list[dir-1][0] * distance
    move_distance_y = move_dir_list[dir-1][1] * distance

    result = list()

    for a,b in cloud_location:
        result.append([(a+move_distance_x)%n,(b+move_distance_y)%n])
    
    return result

#2번동작 - 구름에 물이 내려서 각 칸에 물의 양을 +1씩함.
#1번에서 만든 구름 위치를 주면, 해당 위치값을 +1씩함.
def raining(cloud_location:list):
    for a,b in cloud_location:
        field[a][b] += 1

#3번 동작 - 구름이 사라짐.
#4번 동작 - 물이 증가된 위치에서 대각선으로 물의 거리가 1인 개수만큼 바구니의 물의 양이 늘어남.
#cloud_location은 구름이 이동한 위치.
def field_update(cloud_location:list) -> None:

    #4방향의 대각선중 물이 있는것의 개수를 세서 업데이트
    diagonal = [[-1,-1],[-1,1],[1,-1],[1,1]]

    for current_x,current_y in cloud_location:
        #대각선에 물이 있는 개수 세기
        count = 0
        for a,b in diagonal:
            next_x = current_x + a
            next_y = current_y + b

            #격자판을 넘어서면 안되고 0이면 안됨.
            if (0 <= next_x < n) and (0 <= next_y < n) and field[next_x][next_y] != 0:
                count+=1

        field[current_x][current_y] += count

#5번 동작 - 위에서 사라진 구름이 아니고, 필드에 2이 이상인 위치를 뽑아냄
def new_cloud_location(cloud_location:list)->list:

    #이전의 구름 표시
    for a,b in cloud_location:
        cloud_field[a][b] = 1

    result = list()
    for i in range(n):
        for j in range(n):
            if field[i][j] >= 2 and cloud_field[i][j] == 0:
                field[i][j] -= 2
                result.append([i,j])

    #이전의 구름 위치 0으로 
    for a,b in cloud_location:
        cloud_field[a][b] = 0
    
    return result

#이동
move_list = list()
for _ in range(m):

    dir,distance = map(int,sys.stdin.readline().split())

    #1번
    cloud_location = cloud_move(dir,distance,cloud_location_list)

    #2번
    raining(cloud_location)
    #3번 - 물 사라짐
    #4번
    field_update(cloud_location)

    #5번
    cloud_location_list = new_cloud_location(cloud_location)


print(total_water())