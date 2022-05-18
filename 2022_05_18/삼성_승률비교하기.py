#SWEA 3975번 (싸피,D3)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_18/sample_input.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

num_list = [list(map(int,sys.stdin.readline().split())) for _ in range(T)]

for test_case in range(1, T + 1):

    result = 0


    a,b,c,d = num_list[test_case-1]

    alice = a/b 
    bob = c/d

    if alice > bob:
        result = "ALICE"

    elif alice < bob:
        result = "BOB"

    else:
        result = "DRAW"

    
    print(f"#{test_case} {result}")