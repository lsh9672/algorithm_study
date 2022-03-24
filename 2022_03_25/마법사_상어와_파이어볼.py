#백준 20056번 (구현연습)
import sys
from collections import deque


n,m,k = map(int,sys.stdin.readline().split())

#0: x,1:y,2:m(질량),3:d(방향),4:s(속도)
fireball_info_list = list()

#각각의 파이어볼의 질량과 속도,뱡향을 저장.
#[[[질량,방향,속도],[질량,방향,속도]]]
field = [[deque(list()) for _ in range(n)]for _ in range(n)]

for _ in range(m):
    fireball_info_list.append(list(map(int,sys.stdin.readline().split())))

fireball_location = list()

#초기 파이어볼
for fireball_info in fireball_info_list:
    a,b = fireball_info[0],fireball_info[1]
    m,d,s = fireball_info[2],fireball_info[3],fireball_info[4]

    fireball_location.append([a-1,b-1])

    field[a-1][b-1].append([m,d,s])

#방향 정의
#0,1,2,3,4,5,6,7
move_dir = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

#1번 - d방향으로 s칸만큼 이동
def move_fireball(fireball_location:list) -> list():
    
    #파이어볼의 이동 좌표
    result = list()
    #좌표정보만 꺼내기
    for x,y in fireball_location:
        next_x =0
        next_y = 0

        #해당좌표에서 하나씩 pop() - 리스트 이므로 앞에서 pop이 아닌 뒤에서 pop을 해야 속도에서 이득
        while len(field[x][y]):
            temp_info = field[x][y].popleft()
            
            #방향 꺼내서 매핑
            move_x,move_y = move_dir[temp_info[1]]

            speed = temp_info[2]

            next_x = (x+(move_x * speed)) % n
            next_y = (y+(move_y * speed)) % n


            field[next_x][next_y].append(temp_info)

        result.append((next_x,next_y))

    return result

#2번 - 2개이상인 파이어볼 위치구하고
def two_more_fireball(fireball_location:list) -> list:

    result = list()

    #파이어볼이 2개 이상인 곳 찾기
    for x,y in fireball_location:
        if len(field[x][y]) >= 2:
            result.append([x,y])
    
    return result

#두칸인 곳에서 발생하는 일 - 파이어볼이 나누어짐
def seperation_fireball(two_fireball:list)->None:

    for x,y in two_fireball:
        
        #총질량
        total_m = 0

        #총 속도 
        total_s = 0

        #홀수
        odd_count = 0

        #짝수
        even_count = 0
        
        temp_length = len(field[x][y])
        while temp_length:
            m,d,s = field[x][y].popleft()

            total_m += m
            total_s += s

            #짝수면 짝수 카운트 증가
            if d % 2 == 0:
                even_count += 1
            
            #아니면 홀수 카운트 증가
            else:
                odd_count += 1

        temp_iter = None
        #카운트 둘중 하나라도 0이 있으면 0,2,4,6 아니면 1,3,5,7
        if even_count == 0 or odd_count == 0:
            temp_iter = [0,2,4,6]

        else:
            temp_iter = [1,3,5,7]

        
        #질량이 0이면 사라짐
        if total_m//5 != 0:
            #반복문 돌리면서 파이어볼 4개로 만들기
            for i in temp_iter:
            
                field[x][y].append([total_m//5,i,total_s//temp_length])


#질량의 총합
def mass_total(fireball_location:list)-> int:

    result = 0
    for x,y in fireball_location:
        while len(field[x][y]):
            temp = field[x][y].pop()
            
            result += temp[0]

    return result



fireball_location = list(fireball_location)
# 명령실행
for _ in range(k):

    #파이어볼 이동
    fireball_location = move_fireball(fireball_location)

    two_fireball = two_more_fireball(fireball_location)

    if len(two_fireball) > 0:

        seperation_fireball(two_fireball)


print(mass_total(fireball_location))