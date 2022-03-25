#백준 20056번 (구현연습)
import sys
from collections import deque


n,m,k = map(int,sys.stdin.readline().split())

#0: x,1:y,2:m(질량),3:s(속도),4:d(방향)
fireball_info_list = deque(list())

#각각의 파이어볼의 질량과 속도,뱡향을 저장.
#[[[질량,방향,속도],[질량,방향,속도]]]
field = [[deque(list()) for _ in range(n)]for _ in range(n)]

for _ in range(m):
    fireball_info_list.append(list(map(int,sys.stdin.readline().split())))

#좌표값에 -1씩하기. 
for i in range(m):
    fireball_info_list[i][0] -= 1 
    fireball_info_list[i][1] -= 1

'''실제 로직함수,'''
def solution(fireball_info_list:list) -> int:

    total_result = 0
    #방향 정의
    #0,1,2,3,4,5,6,7
    move_dir = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

    # 명령을 k번 반복
    for _ in range(k):
    

        while fireball_info_list:
            #파이어볼 이동.
            x,y,m,s,d = fireball_info_list.popleft()


            move_x,move_y = move_dir[d]

            next_x = (x+(move_x * s)) % n
            next_y = (y+(move_y * s)) % n

            #좌표평면 업데이트
            field[next_x][next_y].append([m,s,d])

        #2단계
        #2-1 2개인 좌표를 구한.
        for x in range(n):
            for y in range(n):

                #파이어볼이 2개 이상이면 
                if len(field[x][y]) >= 2:
                    #총질량
                    total_m = 0
                    #총 속도 
                    total_s = 0
                    #홀수
                    odd_count = 0
                    #짝수
                    even_count = 0
                    
                    temp_length = len(field[x][y])
                    while len(field[x][y]):
                        m,s,d = field[x][y].popleft()

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
                            fireball_info_list.append([x,y,total_m//5,total_s//temp_length,i])
            
                #1이면 경로 추가.
                elif len(field[x][y]) >= 1:
                    temp = [x,y] + field[x][y].popleft()
                    fireball_info_list.append(temp)

    #명령이 다끝나면 다 돌면서 값 더하기
    for x,y,m,s,d in fireball_info_list:

        total_result += m

    return total_result

print(solution(fireball_info_list))