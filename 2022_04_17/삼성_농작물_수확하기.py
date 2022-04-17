#SWEA 2805번 (싸피,D3)
import sys


sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_04_17/input.txt", "r")

# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):

#     n = int(input())

    
#     farm = list()
#     for _ in range(n):
#         farm.append(input().strip())

#     total = 0 

#     #가운데줄을 제외한 나머지.
#     for i in range((n-1)//2):
        
#         total += int(farm[i][(n-1)//2])
#         #아래에서 올라오는 것
#         total += int(farm[n-1-i][(n-1)//2])
        
#         #양 옆 처리
#         for j in range(i):
#             total += int(farm[i][((n-1)//2)-(j+1)])
#             total += int(farm[i][((n-1)//2)+(j+1)])

#             total += int(farm[n-1-i][((n-1)//2)-(j+1)])
#             total += int(farm[n-1-i][((n-1)//2)+(j+1)])

    
#     #가운데 줄
#     midle_index = (n-1)//2
#     for i in range(n):
#         total += int(farm[midle_index][i])
        
#     print(f"#{test_case} {total}")


'''다른 풀이
구글링을 통해 다른 방식의 풀이를 보고 다시 풀어봄
'''

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_04_17/input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n = int(input())

    
    farm = list()
    for _ in range(n):
        farm.append(input().strip())

    total = 0

    middle_index = (n-1)//2

    start_index = middle_index
    end_index = middle_index

    for i in range(n):

        for j in range(start_index,end_index+1):
            total += int(farm[i][j])

        ##중간지점을 넘어가지 않았으면 점차 증가
        if i < middle_index:
            start_index -=1
            end_index += 1

        ## 중간지점을 넘어갔으면 점차 감소
        else:
            start_index += 1
            end_index -= 1

    print(f"#{test_case} {total}")
