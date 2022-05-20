#SWEA 4676번 (싸피,D3)

import sys


sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_20/sample_input (8).txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    input_string = list(sys.stdin.readline().strip())

    hyphen_num = int(sys.stdin.readline().strip())

    hyphen_loc = list(map(int,sys.stdin.readline().split()))

    hyphen_loc.sort(reverse=True)

    for i in hyphen_loc:
        input_string.insert(i,"-")

    result = "".join(input_string)

    print(f"#{test_case} {result}")