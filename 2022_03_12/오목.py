#백준 2615번(오목, 구현연습)
import sys

omok_field = list()

for _ in range(19):
    omok_field.append(list(map(int,sys.stdin.readline().split())))

visited = [[0 for _ in range(19)] for _ in range(19)]

def omok_check(current_location:list,color:int,find_check_list:list)->int:
    
    #find_check_list => 오른쪽,아래, 오른쪽 아래 대각선, 왼쪽아래 대각선중에 탐색해도 되는지 여부 저장.
    #오른쪽
    move_to_right = [0,1]

    #아래
    move_to_down = [1,0]

    #오른쪽아래 대각선  
    move_to_right_down = [1,1]
    
    #왼쪽 아래 대각선
    move_to_left_down = [1,-1]

    #오른쪽 6칸 확인 - 5목을 넘었는지 여부 확인
    if find_check_list[0] == 0:
        count = 0
        current_x = current_location[0]
        current_y = current_location[1]
        for _ in range(5):
            next_x = current_x + move_to_right[0]
            next_y = current_y + move_to_right[1]

            #오목판을 벗어나는지 여부 확인.
            if (0<= next_x<19) and (0<= next_y<19):
                #현재 위치 업데이트
                current_x = next_x
                current_y = next_y

                if omok_field[current_x][current_y] == color:
                    count+=1
                else:
                    break  
            else:
                break
        
        if count == 4:
            return 1
    

    #아래 6칸 확인
    if find_check_list[1] == 0:
        count = 0
        current_x = current_location[0]
        current_y = current_location[1]
        for _ in range(5):
            next_x = current_x + move_to_down[0]
            next_y = current_y + move_to_down[1]

            #오목판을 벗어나는지 여부 확인.
            if (0<= next_x<19) and (0<= next_y<19):
                #현재 위치 업데이트
                current_x = next_x
                current_y = next_y

                if omok_field[current_x][current_y] == color:
                    count+=1
                else:
                    break  
            else:
                break

        if count == 4:
            return 1

    #오른쪽 아래 대각선 확인
    if find_check_list[2] == 0:
        count = 0
        current_x = current_location[0]
        current_y = current_location[1]
        for _ in range(5):
            next_x = current_x + move_to_right_down[0]
            next_y = current_y + move_to_right_down[1]

            #오목판을 벗어나는지 여부 확인.
            if (0<= next_x<19) and (0<= next_y<19):
                #현재 위치 업데이트
                current_x = next_x
                current_y = next_y

                if omok_field[current_x][current_y] == color:
                    count+=1
                else:
                    break
            else:
                break

        if count == 4:
            return 1

    #왼쪽 아래 대각선 확인
    if find_check_list[3] == 0:
        count = 0
        current_x = current_location[0]
        current_y = current_location[1]
        for _ in range(5):
            next_x = current_x + move_to_left_down[0]
            next_y = current_y + move_to_left_down[1]

            #오목판을 벗어나는지 여부 확인.
            if (0<= next_x<19) and (0<= next_y<19):
                #현재 위치 업데이트
                current_x = next_x
                current_y = next_y

                if omok_field[current_x][current_y] == color:
                    count+=1
                else:
                    break    
            else:
                break

        if count == 4:
            return 2


    return 0



result = None

#왼쪽,위,왼쪽위 대각선,오른쪽 위 대각선
check_move_pre = [[0,-1],[-1,0],[-1,-1],[-1,1]]

#반복문을 돌면서, 0이 아니고, 방문하지 않았으면, 그 위치에서 부터 우측,아래,오른쪽아래 대각선,왼쪽아래 대각선 으로 탐색
for i in range(19):
    for j in range(19):
        #돌이 있고, 탐색하지 않은 돌이라면 탐색시작 
        if omok_field[i][j] != 0 and visited[i][j] == 0:
            visited[i][j] = 1
            
            #만약 왼쪽,왼쪽위 대각선, 위, 오른쪽위 대각선에 자신과 같은 돌이 있으면, 넘어가기
            omok_dol = omok_field[i][j]

            #왼쪽,위,왼쪽위 대각선,오른쪽 위 대각선 => 탐색을 해도 되는지 여부 확인. 0이면 탐색가능
            find_check_list = [1,1,1,1]

            for x in range(4):
                next_check_x = i + check_move_pre[x][0]
                next_check_y = j + check_move_pre[x][1]

                #바둑판을 안넘어가는지 확인
                if (0<=next_check_x<19) and (0<=next_check_y<19):
                    #돌의 색깔이 같은지 확인.- 같으면 해당 부분은 탐색 안해도됨.
                    if omok_field[next_check_x][next_check_y] == omok_dol:
                        continue
                    #돌의 색깔이 다르거나 비어있으면 해당부분은 탐색 
                    else:
                        find_check_list[x] = 0
                #하나만 넘어갔어도 탐색해도됨
                else:
                    find_check_list[x] = 0

            #0이 한개도 없으면 탐색안해도됨.
            if 0 not in find_check_list:
                continue
            
            #가장 위에 있는거, 즉 시작 하는 돌
            result = [i+1,j+1]
            
            #탐색했는데 이겼으면, 출력하고 종료
            omok_check_result = omok_check([i,j], omok_dol,find_check_list)
            if omok_check_result == 1:
                print(omok_dol)
                print(*result)
                exit()
            
            #왼쪽아래대각선이면 왼쪽 끝 좌표를 출력해야됨.
            elif omok_check_result == 2:
                result = [i+1+4, j+1-4]
                print(omok_dol)
                print(*result)
                exit()


#다 탐색할때까지 안끝났으면,0을 출력
print(0)

