#SWEA 5431번 (싸피,d3)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_27/sample_input (13).txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    result = ""
    n,k = map(int,sys.stdin.readline().split())
    num_set = set(map(int,sys.stdin.readline().split()))

    for i in range(1,n+1):
        if i not in num_set:
            result += str(i) + " "



    print(f"#{test_case} {result[:-1]}")