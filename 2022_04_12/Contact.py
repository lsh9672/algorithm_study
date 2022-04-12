#백준 1013번 (문자열, 골드5)
import sys
import re

t = int(sys.stdin.readline())

pattern = re.compile("(100+1+|01)+")



# for _ in range(t):
#     input_pattern = sys.stdin.readline().strip()

#     while True:
        
#         temp = pattern.match(input_pattern)

#         if temp == None:
#             print("NO")
#             break

#         else:
#             end_index = temp.end()
#             if len(input_pattern) == end_index:
#                 print("YES")
#                 break
            
#             else:
#                 input_pattern = input_pattern[end_index:]

for _ in range(t):
    input_value = sys.stdin.readline().strip()

    input_length = len(input_value)

    count_length = 0

    for i in pattern.finditer(input_value):
        count_length += len(i.group())

    
    if input_length == count_length:
        print("YES")

    else:
        print("NO")