#SWEA 1986번 (싸피,D2)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_08/input (19).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0

    n = int(sys.stdin.readline().strip())

    for i in range(1,n+1):
        if i%2 == 0:
            result -= i

        else:
            result += i

    print(f"#{test_case} {result}")