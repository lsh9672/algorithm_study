#백준 5525번 (실버2, 문자열 연습)
'''시간초과난 풀이
import sys

n = int(sys.stdin.readline().strip())

m = int(sys.stdin.readline().strip())

input_value = sys.stdin.readline().strip()

result = 0

target = "IOI"

if n >= 2:
    target += "OI"*(n-1)

for i in range(m-((2*n) +1)):
    if target == input_value[i:i+(2*n)+1]:
        result += 1

print(result)
'''
import sys

n = int(sys.stdin.readline().strip())

m = int(sys.stdin.readline().strip())

input_value = sys.stdin.readline().strip()

result = 0

target = "IOI"

count = 0

count_iter = 0

while count < (m-1):
    if input_value[count:count+3] == target:
        count += 2
        count_iter += 1
        if count_iter == n:
            result += 1
            count_iter -= 1
    
    else:
        count += 1
        count_iter = 0

print(result)

