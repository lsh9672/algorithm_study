#SWEA 1225번(D3, 싸피연습)
import sys
from collections import deque

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_04_27/input (11).txt", "r")


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for _ in range(1, 11):
    test_case = int(input())

    num_list = deque(list(map(int,input().split())))

    count = 1

    result = None

    while True:
        if count > 5:
            count = 1

        first_num = num_list.popleft() - count

        if first_num <= 0:
            num_list.append(0)
            result = num_list
            break
        
        num_list.append(first_num)
        
        count += 1


    print(f"#{test_case}", end=" ")
    print(*result)


