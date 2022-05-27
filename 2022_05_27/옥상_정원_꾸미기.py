#백준 6198번 (자료구조, 골드5)
import sys

n = int(sys.stdin.readline().strip())

building_height = list()

for _ in range(n):
    building_height.append(int(sys.stdin.readline().strip()))


result = 0
stack = list()

for i in range(n):
    
    while len(stack) != 0 and stack[-1] <= building_height[i]:
        stack.pop()

    result += len(stack)
    stack.append(building_height[i])
    

print(result)