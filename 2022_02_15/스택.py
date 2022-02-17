#백준 10828 스택
import sys


test_case = int(sys.stdin.readline())

stack = list()

for _ in range(test_case):

    input_list = list(map(str,sys.stdin.readline().split()))

    if input_list[0] == "push":
        stack.append(int(input_list[1]))

    elif input_list[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    
    elif input_list[0] == "size":
        print(len(stack))

    elif input_list[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif input_list[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
