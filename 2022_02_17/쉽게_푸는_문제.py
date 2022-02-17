#백준 - 쉽게 푸는 문제(실버5)

'''입력'''
import sys

a,b = map(int,sys.stdin.readline().split())

result = list()

total =0

count = 0
check = True
for i in range(1,b+1):
    for j in range(i):
        count+=1
        if count>=3:
            total +=i
        if count == 7:
            check = False
            break
    
    if check == False:
        break
print(total)
