#백준 1935번 (자료구조 연습, 실버3)
import sys

## A: 65
n = int(sys.stdin.readline().strip())

postfix_string = list(sys.stdin.readline().strip())

value_dict = dict()

stack = list()

operator = {"+","-","*","/"}

for i in range(65,65+n):
    value_dict[chr(i)] = int(sys.stdin.readline())

##알파벳 숫자로 변환
for i in range(len(postfix_string)):
    if(postfix_string[i].isalpha()):
        postfix_string[i] = value_dict[postfix_string[i]]


for i in postfix_string:
    if i in operator:
        b = stack.pop()
        a = stack.pop()
        if i =="+":
            stack.append(a+b)
        
        elif i =="-":
            stack.append(a-b)
        
        elif i =="*":
            stack.append(a*b)
        
        else:
            if b == 0:
                print("error")
                break
            else:
                stack.append(a/b)

    else:
        stack.append(i)
print(f"{stack[-1]:0.2f}")