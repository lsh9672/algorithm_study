#백준 15685번 (구현연습, 골드 4)
import sys

n = int(sys.stdin.readline().strip())

dx = [1,0,-1,0]
dy = [0,-1,0,1]

field = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):

    #x,y 방향, 세대
    x,y,d,g = map(int,sys.stdin.readline().split())

    #시작 좌표
    field[x][y] = 1

    #방향 - 다음세대 드래곤 커브 계산을 위해 저장해둬야 됨.
    move_list = [d]

    for _ in range(g):

        temp = list()
        for i in range(len(move_list)):
            temp.append((move_list[-i-1] + 1)%4)

        move_list.extend(temp)

    #방향에 맞춰서 드래곤커브, 좌표평면에 입력
    for i in move_list:
        next_x = x + dx[i]
        next_y = y + dy[i]

        field[next_x][next_y] = 1

        #다음 좌표에 이어붙여야 되기 때문에 업데이트
        x,y = next_x, next_y


#반복문으로 좌표평면을 돌면서 1인 좌표를 만나면 오른쪽, 아래, 오른쪽 아래 대각선을 확인해서 전부 1이 되는지 봄.
#전부 1이면 사각형이므로 count+1
count = 0
for i in range(100):
    for j in range(100):
        if field[i][j] == 1:
            if field[i+1][j] == field[i][j+1] == field[i+1][j+1] == 1:
                count += 1

print(count)



