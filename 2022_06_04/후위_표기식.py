#백준 1918번

import sys

input_string = sys.stdin.readline().strip()

stack = list()

result = ""

for i in input_string:

    ## 알파벳이면 결과변수에 이어붙임
    if i.isalpha():
        result += i

    ## 알파벳이 아니면, 연산자, 괄호의 경우를 다 따져줘야됨
    else:

        ## 여는 괄호면 그냥 스택에 넣음
        if i == "(":
            stack.append("(")

        ## *와 /일떄
        elif i == "*" or i == "/":
            while len(stack) != 0 and (stack[-1] == "*" or stack[-1] == "/"):
                result += stack.pop()

            stack.append(i)

        ## + 와 - 일때
        elif i == "+" or i == "-":
            while len(stack) != 0 and stack[-1] != "(":
                result += stack.pop()

            stack.append(i)
        
        ## 닫는 괄호일떄 - 여는 괄호가 나올떄까지 팝함
        elif i == ")":
            while len(stack) != 0 and stack[-1] != "(":
                result += stack.pop()

            ##여는 괄호가 스택안에 남아있기 때문에 빼줌
            stack.pop() 

##스택안에 남아있는 것들을 뺴서 결과 변수에 이어 붙여줌
while len(stack) != 0:
    result += stack.pop()

print(result)