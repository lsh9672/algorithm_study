##SWEA 1288번(싸피,D2)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_04_29/sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n = int(sys.stdin.readline())
    
    count = 1

    check = set()

    while True:
        temp = str(count*n)

        for i in temp:
            check.add(i)

        if len(check) == 10:
            break

        count+=1

    print(f"#{test_case} {count*n}")