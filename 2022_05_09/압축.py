#백준 1662번 (자료구조, 골드5)
import sys


s = sys.stdin.readline().strip()

stack = list()

temp_count = 0

temp_num = 1
for i in s:

    if i.isdigit():
        temp_count += 1

        ## 여는 괄호가 나오면 그 안의 길이와 곱해야되기 때문에 마지막 숫자를 계속 세이브하고 있음
        temp_num = i
    

    elif i == "(":
        ## [곱할수, 곱할수 전까지의 길이(더해야되는 수)]
        stack.append([temp_num,temp_count-1])

        temp_count = 0

    else:
        ## 닫는괄호가 나오면 저장된 것 꺼냄

        a,b= stack.pop()


        temp_count = (int(a) * temp_count) + b

print(temp_count)
