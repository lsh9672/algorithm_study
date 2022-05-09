#SWEA 2001번 (싸피,D2)

import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_08/input (21).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0

    n,m = map(int,sys.stdin.readline().split())

    field = list()

    for _ in range(n):
        field.append(list(map(int,sys.stdin.readline().split())))

    
    for i in range(n-m+1):
        for j in range(n-m+1):
            temp = 0
            for x in range(i,i+m):
                for y in range(j,j+m):
                    temp += field[x][y]
            
            result = max(result,temp)


    print(f"#{test_case} {result}")