# SWEA 4522 (싸피,D3)
import sys


sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_19/sample_input (5).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    result = "Not exist"
    
    input_string = sys.stdin.readline().strip()

    start = 0
    end = len(input_string) -1

    while start < end:

        if input_string[start] != input_string[end]:
            ## 둘다 물음표가 아닌지 확인
            if input_string[start] != "?" and input_string[end] != "?":
                break

        
        start += 1

        end -= 1
    ##중간에 브레이크로 빠저나오지 않고 끝까지 탐색했으면
    else:
        result = "Exist"

    

    print(f"#{test_case} {result}")