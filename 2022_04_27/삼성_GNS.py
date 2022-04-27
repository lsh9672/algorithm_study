##SWEA 1221번 (D3, 싸피대비)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_04_27/GNS_test_input.txt", "r")


T = int(input())

num_dict = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a,b = input().split()

    input_num = input().split()

    input_num.sort(key = lambda x : num_dict[x])

    print(a)
    print(*input_num)