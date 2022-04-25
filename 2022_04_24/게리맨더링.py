#백준 17779번 (골드4, 시뮬레이션 연습)
import sys


n = int(sys.stdin.readline())

field = [[0 for _ in range(n+1)]]

total_people = 0

for i    in range(n):
    temp_list = [0] + list(map(int,sys.stdin.readline().split()))

    field.append(temp_list)
    total_people += sum(temp_list)

## 선거구 5를 나누는 함수 - 경계선만 채우면 됨, 경계썬 안쪽은 0인데, 나머지 선거구를 1,2,3,4로 표시할것이므로 
## 불필요하게 안을 채울필요 없음 - 1,2,3,4 들의 값 구하고 전체에ㅓ 뺴면됨
def district_5(temp_field:list,x:int,y:int,d1:int,d2:int,people_num:list)->None:


    #경계선  - 5번 선거구
    ## (x, y), (x+1, y-1), ..., (x+d1, y-d1)
    ## (x, y), (x+1, y+1), ..., (x+d2, y+d2)
    ## (x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
    ## (x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)


    for i in range(d1+1):
        temp_field[x+i][y-i] = 5
        temp_field[x+d2+i][y+d2-i] = 5

    for i in range(d2+1):
        temp_field[x+i][y+i] = 5
        temp_field[x+d1+i][y-d1+i] = 5


## 선거구 1를 나누는 함수 - 해당하는 선걱를 전부 1로 채움
def district_1(temp_field:list,x,y,d1,d2,people_num:list)->None:
    ## 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y

    for i in range(1,x+d1):
        for j in range(1,y+1):
            if temp_field[i][j] == 5:
                break
            else:
                temp_field[i][j] = 1
                people_num[0]+=field[i][j]

## 선거구 2를 나누는 함수 - 해당하는 선걱를 전부 2로 채움
def district_2(temp_field:list,x,y,d1,d2,people_num:list)->None:
    
    ## 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N

    temp_total = 0
    for i in range(1,x+d2+1):
        for j in range(n,y,-1):
            if temp_field[i][j] == 5:
                break
            else:
                temp_field[i][j] = 2
                people_num[1]+=field[i][j]



## 선거구 3를 나누는 함수 - 해당하는 선걱를 전부 3로 채움
def district_3(temp_field:list,x,y,d1,d2,people_num:list)->None:
    ## 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2

    temp_total = 0
    for i in range(x+d1,n+1):
        for j in range(1,y-d1+d2):
            if temp_field[i][j] == 5:
                break
            else:
                temp_field[i][j] = 3
                people_num[2]+=field[i][j]


## 선거구 4를 나누는 함수 - 해당하는 선걱를 전부 4로 채움
def district_4(temp_field:list,x,y,d1,d2,people_num:list)->None:

    ## 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
    temp_total = 0
    for i in range(x+d2+1,n+1):
        for j in range(n,y-d1+d2-1,-1):
            if temp_field[i][j] == 5 :
                break
            else:
                temp_field[i][j] = 4
                people_num[3]+=field[i][j]


result = 999999

## d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N
for x in range(1,n+1):
    for y in range(1,n+1):
        for d1 in range(1,n+1):
            for d2 in range(1,n+1):
                if x+d1+d2 > n:
                    continue

                if y-d1 < 1 or y+d2 > n:
                    continue

                ## 선거구 채우기
                temp_field = [[0 for _ in range(n+1)] for _ in range(n+1)]
                people_num = [0 for _ in range(5)]
            
                district_5(temp_field,x,y,d1,d2,people_num)
                district_1(temp_field,x,y,d1,d2,people_num)
                district_2(temp_field,x,y,d1,d2,people_num)
                district_3(temp_field,x,y,d1,d2,people_num)
                district_4(temp_field,x,y,d1,d2,people_num)

                # for i in temp_field:
                #     print(i)
                # print("------------------------")

                people_num[4] = total_people - sum(people_num)

                temp_max = max(people_num)
                temp_min = min(people_num)

                result = min(result, temp_max - temp_min)

print(result)