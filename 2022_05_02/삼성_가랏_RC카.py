#SWEA 1940번(D2, 싸피대비)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_02/input (3).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    case = int(sys.stdin.readline().strip())
    
    result = 0
    
    current_speed = 0

    for _ in range(case):
        temp = list(map(int,sys.stdin.readline().split()))

        if temp[0] == 0:
            pass
        
        elif temp[0] == 1:
            current_speed += temp[1]

        else:
            current_speed -= temp[1]
            if current_speed < 0 :
                current_speed = 0
            
            
        result += current_speed

    print(f"#{test_case} {result}")
