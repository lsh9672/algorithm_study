#SWEA 3499 (싸피,D3)
import sys


sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_17/sample_input (16).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    
    n = int(sys.stdin.readline().strip())

    card_list = sys.stdin.readline().split()

    up_list = list()

    down_list = list()

    result = list()

    if n%2 == 0:
        up_list = card_list[:n//2]
        down_list = card_list[n//2:]
    else:
        up_list = card_list[:n//2]
        down_list = card_list[n//2 + 1:]

    for i in range(n//2):

        result.append(up_list[i])
        result.append(down_list[i])
        
    if n%2 == 1:
        result.append(card_list[n//2])

    print(f"#{test_case}" , end = " ")
    print(*result)



