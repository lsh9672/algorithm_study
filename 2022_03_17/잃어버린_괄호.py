#백준 1541번(실버2)
import sys


n = sys.stdin.readline().strip().split("-")

result = 0
if "+" in n[0]:
    temp_list = n[0].split("+")
    temp = 0
    for x in temp_list:
        temp += int(x)
    result = temp
else:
    result = int(n[0])

for i in range(1,len(n)):
    
    if "+" in n[i]:
        temp_list = n[i].split("+")
        temp =0
        for x in temp_list:
            temp+=int(x)
        
        result -= temp
    
    else:
        result -= int(n[i])


print(result)