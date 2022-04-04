#백준 2504번(자료구조 연습)
import sys


bracket = sys.stdin.readline().strip()

check_bracket_stack = list()

result = 0

temp = 1

prev_bracket = ""
for i in bracket:
    
    if i == "(":
        check_bracket_stack.append(i)
        temp *=2

    elif i == "[":
        check_bracket_stack.append(i)
        temp *= 3


    elif i == ")":
        if len(check_bracket_stack) == 0 or check_bracket_stack[-1] == "[":
            result = 0
            break
        
        elif prev_bracket == "(":
            result += temp

        check_bracket_stack.pop()
        temp //= 2


    else:
        if len(check_bracket_stack) == 0 or check_bracket_stack[-1] == "(":
            result = 0
            break
        
        elif prev_bracket == "[":
            result += temp
        
        check_bracket_stack.pop()
        temp //= 3

    prev_bracket = i

if len(check_bracket_stack) == 0:
    print(result)

else:
    print(0)