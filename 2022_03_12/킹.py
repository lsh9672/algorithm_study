#백준 1063 킹 (구현연습)
import sys

king,rock, n = map(str,sys.stdin.readline().split())

chess_field = [[0 for _ in range(8)] for _ in range(8)] 

#체스판좌표를 좌표평면에 맞게 변환해주는 함수
def change_coordinates(cor:str) -> list:
    alpha_to_num = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7}

    return [8-int(cor[1]),alpha_to_num[cor[0]]]

#좌표평면에 맞는 좌표를 체스판 좌표로 변경
def reverse_change_coordinates(cor:list)-> str:
    num_to_alpha = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H"}

    result = num_to_alpha[cor[1]]+str(8-cor[0])

    return result
#이동 좌표정의

move_command = {"R":[0,1],"L":[0,-1],"B":[1,0],"T":[-1,0],"RT":[-1,1],"LT":[-1,-1],"RB":[1,1],"LB":[1,-1]}

current_king_x,current_king_y = change_coordinates(king)
current_rock_x,current_rock_y = change_coordinates(rock)

#초기 킹과 돌을 좌표평면에 놓는다.
#킹은 2, 돌은 1로 표시, 빈칸은 0
chess_field[current_king_x][current_king_y] = 2
chess_field[current_rock_x][current_rock_y] = 1

for _ in range(int(n)):

    command = move_command[sys.stdin.readline().strip()]

    next_x = current_king_x+ command[0]
    next_y = current_king_y + command[1]

   
    
    #킹을 이동시켰을때 체스판을 안넘어기는지 확인.
    if (0 <= next_x < 8) and (0 <= next_y < 8):
        
        #돌쪽 이동이라면,
        if  chess_field[next_x][next_y] == 1:
            
            next_rock_x = current_rock_x + command[0]
            next_rock_y = current_rock_y + command[1]

            #돌을 이동시켰을때, 체스판을 벗어나는지 확인
            if (0 <= next_rock_x < 8) and (0 <= next_rock_y < 8):

                #벗어나지 않으면
                chess_field[next_rock_x][next_rock_y] = 1
                chess_field[next_x][next_y] = 2

                chess_field[current_king_x][current_king_y] = 0

                current_king_x = next_x
                current_king_y = next_y
                current_rock_x = next_rock_x
                current_rock_y = next_rock_y
            
            #체스판을 벗어나면패스
            else:
                continue
        #돌쪽으로 이동이 아닐때
        else:
            #벗어나지 않으면
            chess_field[next_x][next_y] = 2
            chess_field[current_king_x][current_king_y]  = 0

            current_king_x = next_x
            current_king_y = next_y

    #체스판을 넘어가면 패스        
    else:
        continue



print(reverse_change_coordinates([current_king_x,current_king_y]))
print(reverse_change_coordinates([current_rock_x,current_rock_y]))





