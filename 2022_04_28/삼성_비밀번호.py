#SWEA 1234번 (싸피,D3)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_04_28/input (15).txt", "r")


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):

    n,temp = input().split()

    stack = list()

    for i in temp:
        if len(stack) == 0:
            stack.append(i)

        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    
    result = "".join(stack)

    print(f"#{test_case} {result}")