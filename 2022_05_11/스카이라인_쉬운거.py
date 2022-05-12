#1863번 (자료구조, 골드5)
from distutils.command.build import build
import sys

n = int(sys.stdin.readline().strip())


stack = list()

building_count = 0

for _ in range(n):

    x,y = map(int,sys.stdin.readline().split())

    if y== 0:
        stack = list()
        continue

    ##스택이 비었으면 그냥 넣음
    if len(stack) == 0:
        stack.append(y)
        building_count += 1
    
    ##스택이 비어있지 않다면,
    else:
        if stack[-1] > y:
            ##직전의 높이보다 낮아지면, 자신의 높이보다 낮지 않을때까지 다 뻄
            while len(stack) > 0 and stack[-1] > y:
                stack.pop()

            if len(stack)>0 and stack[-1] == y:
                # print(f"y : {y}, building_count : {building_count}")
                continue

            elif len(stack) == 0 or stack[-1] < y:
                stack.append(y)
                building_count += 1
            
        
        elif stack[-1] < y:
            building_count += 1
            stack.append(y)

        else:
            # print(f"y : {y}, building_count : {building_count}")
            continue

    # print(f"y : {y}, building_count : {building_count}")

print(building_count)




