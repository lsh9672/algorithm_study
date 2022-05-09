#백준 9935번 (자료구조, 골드4)
'''구글링 해서 참고한 코드 '''
import sys

origin_str = sys.stdin.readline().strip()

boom_str = sys.stdin.readline().strip()

stack = list()

result = ""

last_boom_str = boom_str[-1]
length_boom_str = len(boom_str)

for i in origin_str:

    stack.append(i)

    if stack[-1] == last_boom_str:
        temp = "".join(stack[-length_boom_str:])

        if temp == boom_str:
            del stack[-length_boom_str:]

    
if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))                                                                         