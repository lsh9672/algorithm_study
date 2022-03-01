#백준 ABC 브론즈2

import sys

num_list = list(map(int,sys.stdin.readline().split()))


num_list.sort()

sort_alpha = sys.stdin.readline()

result = ""

for i in sort_alpha:
    if i == "A":
        result += str(num_list[0])+" "

    elif i == "B":
        result += str(num_list[1])+" "

    elif i == "C":
        result += str(num_list[2])+" "

print(result)