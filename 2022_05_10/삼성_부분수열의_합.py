#SWEA 2817번 (싸피, D3)
'''
조합을 이용한 완탐은 시간초과가 남,
재귀를 이용해서 풀어야 됨.
'''

# import sys
# from itertools import combinations

# sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_10/sample_input (1).txt", "r")

# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     result = 0

#     n,k = map(int,sys.stdin.readline().split())

#     num_list = list(map(int,sys.stdin.readline().split()))


#     for i in range(n):
#         temp = combinations(num_list,i)

#         for j in list(temp):
#             if sum(j) == k:
#                 result += 1

#     print(f"#{test_case} {result}")


import sys


sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_10/sample_input (1).txt", "r")


def recursive(index:int,sum:int):
    global result

    if index >= n:
        return

    temp = sum + num_list[index]

    if temp == k:
        result += 1

    ## 이전꺼 안더하고 진행
    recursive(index+1,sum)

    ##이전꺼 더하고 진행
    recursive(index+1,temp)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0

    n,k = map(int,sys.stdin.readline().split())

    num_list = list(map(int,sys.stdin.readline().split()))

    recursive(0,0)


    print(f"#{test_case} {result}")