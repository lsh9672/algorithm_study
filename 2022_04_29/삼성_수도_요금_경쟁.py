##SWEA 1284번 (D2)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_04_29/input.txt", "r")


T = int(input())
for test_case in range(1, T + 1):

    result = 0

    p,q,r,s,w = map(int,input().split())

    a_company = p*w

    b_company = 0
    if w <= r:
        b_company = q
    else:

        b_company = q + (w-r)*s

    result = min(a_company,b_company)

    print(f"#{test_case} {result}")