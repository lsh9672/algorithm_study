#백준 16235번(시뮬레이션 연습)
import sys
from collections import deque


n,m,k = map(int, sys.stdin.readline().split())

#나무 초기 양분
field = [[5 for _ in range(n)] for _ in range(n)]

tree_field = [[deque([]) for _ in range(n)] for _ in range(n)]

#로봇이 줄 양분
tree_nutrient_list = []


dx = [0,0,-1,1,-1,1,-1,1]
dy = [-1,1,0,0,1,-1,-1,1]


for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    tree_nutrient_list.append(temp)

for i in range(m):
    #x,y,나무의 나이
    x,y,age = map(int,sys.stdin.readline().split())

    tree_field[x-1][y-1].append(age)


year = 0

while year < k:

    #시간단축을 위해서 봄을 처리하면서 여름도 같이 처리함.
    #봄, 여름
    #나이가 -1이면 죽은 것으로 간주.
    for i in range(n):
        for j in range(n):
            #1. 봄

            #죽은 나무의 좌표를 저장했다가 업데이트함.
            die_tree_value = 0 

            temp_length =len(tree_field[i][j])
            #나무가 있으면, 양분을 먹음
            if temp_length != 0:
                #작은 나무부터 순차적으로 양분을 먹음.
                for z in range(temp_length):

                    if tree_field[i][j][z] <= field[i][j]:
                        field[i][j] -= tree_field[i][j][z]
                        tree_field[i][j][z] += 1


                    #만약 나무가 먹을수 없어서 죽으면, - 여기서 팝하고 바로 더해도 문제가 없는 이유가
                    #번식 시점에 appendleft를 이용해서 넣을 것이므로, 오름차순으로 정렬되어있고,
                    #오름차순으로 정렬되어있기 때문에, 나무가 죽으면, 그 뒤에 있는 것들도 다 죽기 때문,
                    else:
                        for t in range(z,temp_length):
                            die_tree_value += (tree_field[i][j].pop())//2
                        
                        break

            #2. 여름
            #하나의 위치에서 작업이 끝나면 해당위치의 양분 업데이트
            field[i][j] += die_tree_value


    #시간단축을 위해서 가을을 처리하면 겨울을 처리함.
    #가을,겨울
    # 나무가 번식하게 된다.
    for i in range(n):
        for j in range(n):
            for y in tree_field[i][j]:
                #나무의 나이가 5의 배수인지 확인
                #5의 배수이면 번식
                if y % 5 == 0:
                    for t in range(8):
                        #번식한 나무를 추가할때는 appendleft()를 사용해서 오름차순을 유지 할수 있도록 함.
                        next_x = i + dx[t]
                        next_y = j + dy[t]
                        #좌표평면을 벗어나지 않는지 확인필요
                        if (0 <= next_x < n) and (0 <= next_y < n):
                            tree_field[next_x][next_y].appendleft(1)

            #겨울에는 로봇이 양분을 추가해줌.
            field[i][j] += tree_nutrient_list[i][j]


    year += 1


result = 0
#다끝나면 반복문을 돌면서 나무의 개수를 센다.
for i in range(n):
    for j in range(n):
        temp = len(tree_field[i][j])
        if temp != 0:
            result += temp



print(result)