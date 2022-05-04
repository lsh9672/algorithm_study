#SWEA 1961번(싸피,D2)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_04/input (11).txt", "r")


def rotate_array(n:int,origin_array:list,change_array:list)->None:

    for i in range(n):
        for j in range(n):
            change_array[j][n-i-1] = origin_array[i][j]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input().strip())

    num_array = list()

    for _ in range(n):
        num_array.append(list(map(int,input().split())))


    first_array = [[0 for _ in range(n)] for _ in range(n)]
    second_array = [[0 for _ in range(n)] for _ in range(n)]
    third_array = [[0 for _ in range(n)] for _ in range(n)]

    rotate_array(n,num_array,first_array)
    rotate_array(n,first_array,second_array)
    rotate_array(n,second_array,third_array)

    print(f"#{test_case}")
    for i in range(n):
        print(f"{''.join(list(map(str,first_array[i])))} {''.join(list(map(str,second_array[i])))} {''.join(list(map(str,third_array[i])))}")



    
