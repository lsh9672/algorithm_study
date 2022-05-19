#SWEA 4751번 (싸피,D3)
import sys


sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_19/sample_input (7).txt", "r")

dir= [[-2,0],[2,0],[0,-2],[0,2],[-1,-1],[-1,1],[1,-1],[1,1]]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    input_string = sys.stdin.readline().strip()

    row_length = 4*len(input_string)+1

    field = [["." for _ in range(row_length)] for _ in range(5)]

    for i in range(len(input_string)):

        str_x = 2
        str_y = 2 + 4*i

        field[str_x][str_y] = input_string[i]

        for x,y in dir:
            next_x = str_x + x
            next_y = str_y + y

            field[next_x][next_y] = "#"

        
    result = ""

    for i in field:
        result += "".join(i)
        result += "\n"

    print(result[:-1])
            




