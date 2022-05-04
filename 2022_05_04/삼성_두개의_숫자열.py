## SWEA 1959번(싸비,D2)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_04/input (10).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m = map(int,input().split())

    a_list = list(map(int,input().split()))

    b_list = list(map(int,input().split()))

    result = 0

    if n > m :
        n,m = m,n
        a_list,b_list = b_list,a_list

    for i in range(m-n+1):
        temp = 0
        for j in range(n):
            temp += a_list[j] * b_list[j+i]

        result = max(temp,result)

    print(f"#{test_case} {result}")


