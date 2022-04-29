#백준 3986번 (실버4,자료구조)
import sys

n = int(sys.stdin.readline())

result_count = 0

for _ in range(n):
    temp = sys.stdin.readline().strip()

    stack = list()

    for i in temp:
        if len(stack) == 0:
            stack.append(i)

        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        
    if len(stack) == 0:
        result_count+=1


print(result_count)