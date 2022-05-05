#SWEA 1970번 (싸피, D2)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_05/input (13).txt", "r")

T = int(input())

money_list = [50000,10000,5000,1000,500,100,50,10]
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = list()
    money = int(sys.stdin.readline().strip())

    for i in money_list:
        result.append(money//i)

        money %= i


    print(f"#{test_case}")
    print(*result)