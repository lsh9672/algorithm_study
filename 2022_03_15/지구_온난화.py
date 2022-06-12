#백준 5212번(구현연습)
'''주의할 점'''
#주어진 r,c가 다가 아니라 테투리는 전부 바다임
#  .....
#  x.x..
#  .....
# 위와같이 주어지면 실제로는 아래와 같은 것.
#  ......
#  .x.x..
#  ......
import sys


r,c = map(int,sys.stdin.readline().split())

dado_map = list()

for _ in range(r):

    dado_map.append(list(sys.stdin.readline().strip()))

#바다로 만들 위치를 한번에 바꿔야 되기 때문에 모아뒀다 바꿈.
delete_location = list()

#상하 좌우 정의
dx = [0,0,-1,1]
dy = [-1,1,0,0]

#주변바다가 3개 이상 있는지 확인.
def delete_check(location:list)-> bool:
    count = 0
    for i in range(4):
        next_x = location[0] + dx[i]
        next_y = location[1] + dy[i]

        #범위를 벗어나면 바다임.
        if next_x < 0 or next_x >=r or next_y < 0  or next_y >=c:
            count+=1

        elif dado_map[next_x][next_y] == ".":
            count +=1
        

    if count >=3:
        return True

    return False
        

for i in range(r):
    for j in range(c):
        #육지면 상하좌우 바다의 개수 세기 - 3이상이면 삭제할 좌표로 저장
        if dado_map[i][j] == "X":
            #3면이상이 바다인지 확인.
            if delete_check([i,j]) == True:
                delete_location.append([i,j])

#삭제할 좌표를 하나씩 꺼내서 지도를 업데이트
for a,b in delete_location:
    dado_map[a][b] = "."


update_land_list = list()

for i in range(r):
    for j in range(c):
        if dado_map[i][j] == "X":
            update_land_list.append([i,j])

#x좌표를 오름차순 정렬 - 제일 작은 값: 0번째 인덱스, 제일 큰 값: 뒤에서 첫번째 값.
x_sort = sorted(update_land_list, key = lambda x : x[0])
update_min_x = x_sort[0][0]
update_max_x = x_sort[-1][0]

#y좌표를 오름차순 정렬,
y_sort = sorted(update_land_list, key = lambda x : x[1])
update_min_y = y_sort[0][1]
update_max_y = y_sort[-1][1]

#삭제할 필요 없이, 위에서 구한 범위를 출력하면 됨.
for i in range(update_min_x,update_max_x+1):
    temp = ""
    for j in range(update_min_y,update_max_y+1):
        temp+=dado_map[i][j]
    print(temp)
