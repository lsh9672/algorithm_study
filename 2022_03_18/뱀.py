#백준 - 3190번 (골드5, 시뮬레이션 연습)
import sys
from collections import deque


n = int(sys.stdin.readline())

#사과 좌표
apple_num = int(sys.stdin.readline())

#사과위치
apple_location = list()

for _ in range(apple_num):
    apple_location.append(list(map(int,sys.stdin.readline().split())))

#뱀의 변환 횟수
snake_conversion_num = int(sys.stdin.readline())

#뱀의 변환 정보
snake_conversion_info = list()

for _ in range(snake_conversion_num):
    snake_conversion_info.append(list(map(str,sys.stdin.readline().split())))


#사과있는 필드
field = [[0 for _ in range(n)] for _ in range(n)]

#필드에 사과 셋팅 - 사과는 -1로 표시, 0,0부터 시작이어서 -1
for a,b in apple_location:
    field[a-1][b-1] = -1

#뱀위치
field_snake = [[0 for _ in range(n)] for _ in range(n)]

#뱀 시작 위치 셋팅, -1로 표시
field_snake[0][0] = -1

#뱀의 좌표를 모아둠.
snake_location = deque(list())

#처음 시작 좌표 넣기
snake_location.appendleft([0,0])

#이동방향
move_dir = (0,1)

#방향 회전했을때의 경우 모음 L:0번째, D:1번째
move_dir_rotate_dict = {(0,1):[(-1,0),(1,0)],(0,-1):[(1,0),(-1,0)],(1,0):[(0,1),(0,-1)],(-1,0):[(0,-1),(0,1)]}

#시간
time_count = 0


for time,dir in snake_conversion_info:

    for _ in range(int(time)-time_count):
        #시간증가
        time_count+=1

        #헤드를 꺼냄.
        current_x,current_y = snake_location[0]

        #헤드에서 현재 방향으로 전진
        next_x = current_x + move_dir[0]
        next_y = current_y + move_dir[1]

        #만약 자기 몸에 부딪히거나, 칸을 벗어나면, 현재 시간 출력하고 프로그램 종료
        if next_x < 0 or next_x >= n or next_y < 0 or next_y >=n or field_snake[next_x][next_y] == -1:
            print(time_count)
            exit()
        
        #위의 조건을 만족하지 않고, 사과이면, 뱀의 대가리 값을 방향쪽으로 증가시킨 값을 앞에 넣음
        elif field[next_x][next_y] == -1:
            snake_location.appendleft([next_x,next_y])
            field_snake[next_x][next_y] = -1
            field[next_x][next_y] = 0

        
        #사과가 아니라면, 뱀의 대가리 값을 방향쪽으로 증가시킨 값을 앞에 넣고 꼬리를 pop
        else:
            snake_location.appendleft([next_x,next_y])
            field_snake[next_x][next_y] = -1

            temp_x,temp_y = snake_location.pop()
            field_snake[temp_x][temp_y] = 0


    #방향전환 로직,
    #위의 시간동안 이동이 끝나면, 방향을 전환해야됨
    if dir == "L":
        move_dir = move_dir_rotate_dict[move_dir][0]
    elif dir == "D":
        move_dir = move_dir_rotate_dict[move_dir][1]


#만약 위의 과정을 거쳤는데도 끝나지 않았다면 끝날때까지 앞으로 이동.
while True:
    time_count+=1

    #헤드를 꺼냄.
    current_x,current_y = snake_location[0]

    #헤드에서 현재 방향으로 전진
    next_x = current_x + move_dir[0]
    next_y = current_y + move_dir[1]

    #만약 자기 몸에 부딪히거나, 칸을 벗어나면, 현재 시간 출력하고 프로그램 종료
    if next_x < 0 or next_x >= n or next_y < 0 or next_y >=n or field_snake[next_x][next_y] == -1:
        print(time_count)
        exit()

    #위의 조건을 만족하지 않고, 사과이면, 뱀의 대가리 값을 방향쪽으로 증가시킨 값을 앞에 넣음
    elif field[next_x][next_y] == -1:
        snake_location.appendleft([next_x,next_y])
        field_snake[next_x][next_y] = -1

    
    #사과가 아니라면, 뱀의 대가리 값을 방향쪽으로 증가시킨 값을 앞에 넣고 꼬리를 pop
    else:
        snake_location.appendleft([next_x,next_y])
        field_snake[next_x][next_y] = -1

        temp_x,temp_y = snake_location.pop()
        field_snake[temp_x][temp_y] = 0

