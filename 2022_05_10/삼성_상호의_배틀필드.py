#SWEA 1873번 (싸피,d3)

import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_10/input.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    h,w = map(int,sys.stdin.readline().split())

    field = list()

    tank_loc_h = 0
    tank_loc_w = 0
    tank = set(["^","<",">","v"])

    for _ in range(h):

        field.append(list(sys.stdin.readline().strip()))

    n = int(sys.stdin.readline().strip())

    commands = sys.stdin.readline().strip()

    ## 초기 탱크위치 찾기
    check = False
    for i in range(h):
        for j in range(w):
            if field[i][j] in tank:
                tank_loc_h = i
                tank_loc_w = j
                check = True
                break
        if check == True:
            break
    
    
    ## 명령어 한개씩 돌려가면서 실행
    for command in commands:
        
        if command == "U":
            field[tank_loc_h][tank_loc_w] = "^"
            next_h = tank_loc_h - 1
            next_w = tank_loc_w

            if next_h >= 0 and field[next_h][next_w] == ".":
                field[tank_loc_h][tank_loc_w] = "."
                field[next_h][next_w] = "^"
                tank_loc_h = next_h
                tank_loc_w = next_w
        
        elif command == "D":
            field[tank_loc_h][tank_loc_w] = "v"
            next_h = tank_loc_h + 1
            next_w = tank_loc_w

            if next_h < h and field[next_h][next_w] == ".":
                field[tank_loc_h][tank_loc_w] = "."
                field[next_h][next_w] = "v"
                tank_loc_h = next_h
                tank_loc_w = next_w
        
        
        elif command == "L":
            field[tank_loc_h][tank_loc_w] = "<"
            next_h = tank_loc_h
            next_w = tank_loc_w -1

            if next_w >= 0 and field[next_h][next_w] == ".":
                field[tank_loc_h][tank_loc_w] = "."
                field[next_h][next_w] = "<"
                tank_loc_h = next_h
                tank_loc_w = next_w
        

        elif command == "R":
            field[tank_loc_h][tank_loc_w] = ">"
            next_h = tank_loc_h
            next_w = tank_loc_w + 1

            if next_w < w and field[next_h][next_w] == ".":
                field[tank_loc_h][tank_loc_w] = "."
                field[next_h][next_w] = ">"
                tank_loc_h = next_h
                tank_loc_w = next_w
        
        elif command == "S":
            dir_h = 0
            dir_w = 0
            if field[tank_loc_h][tank_loc_w] == "^":
                dir_h = -1

            elif field[tank_loc_h][tank_loc_w] == "v":
                dir_h = 1

            elif field[tank_loc_h][tank_loc_w] == "<":
                dir_w = -1

            elif field[tank_loc_h][tank_loc_w] == ">":
                dir_w = 1

            temp_h = tank_loc_h
            temp_w = tank_loc_w
            while True:
                
                temp_h += dir_h
                temp_w += dir_w

                ##게임밖으로 나가면 끝
                if temp_h < 0 or temp_h >= h or temp_w < 0 or temp_w >= w:
                    break
                
                ##벽돌로 만들어진 벽이면 부수고 끝
                elif field[temp_h][temp_w] == "*":
                    field[temp_h][temp_w] = "."
                    break
                
                ## 강철로 만들어진 벽이면 끝
                elif field[temp_h][temp_w] == "#":
                    break
        
    
    print(f"{test_case} {''.join(field[0])}")
    for x in range(1,h):
        print("".join(field[x]))