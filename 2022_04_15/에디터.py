#백준 1406번 (실버2, 자료구조 연습)

import sys

#커서의 왼쪽 - 시작값을 넣어줌
left_stack = list(sys.stdin.readline().strip())

n = int(sys.stdin.readline())

#커서의 오른쪽
right_stack = list()

for _ in range(n):
    command = list(sys.stdin.readline().split())

    if command[0] == "L":
        if len(left_stack) != 0:
            right_stack.append(left_stack.pop())
    
    elif command[0] == "D":
        if len(right_stack) != 0:
            left_stack.append(right_stack.pop())
    
    elif command[0] == "B":
        if len(left_stack) != 0:
            left_stack.pop()

    elif command[0] == "P":
        input_value = command[1]

        left_stack.append(input_value)
    
print("".join(left_stack) + "".join(right_stack[::-1]))

