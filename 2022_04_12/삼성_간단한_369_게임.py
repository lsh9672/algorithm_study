#SWEA 1926번(싸피 대비, D2)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_04_12/input.txt","r")

num_list = ["3","6","9"]

n = int(input())

result = list()

for i in range(1,n+1):
    temp = str(i)
    count = 0

    for j in temp:
        if j in num_list:
            count+=1
        
    if count == 0:
        result.append(temp)

    else:
        result.append("-"*count)

print(*result)