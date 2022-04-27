#SWEA 1220번(싸피대비, D3)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_04_27/input (10).txt", "r")



# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    ##테이블 길이
    n = int(input())

    field = list()
    for _ in range(n):
        field.append(list(map(int,input().split())))
    
    ## 세로줄 탐색
    ##1:N, 2:S
    result_count = 0

    for i in range(n):
        stack = list()
        for j in range(n):
            if field[j][i] == 1 and len(stack) == 0:
                stack.append(1)

            elif field[j][i] == 2 and len(stack) != 0:
                stack.pop()
                result_count += 1

    

    print(f"#{test_case} {result_count}")
