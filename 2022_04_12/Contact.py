#백준 1013번 (문자열, 골드5)
import sys
import re

t = int(sys.stdin.readline())

pattern = re.compile("(100+1+|01)+")

for _ in range(t):
    input_pattern = sys.stdin.readline().strip()

    temp = pattern.fullmatch(input_pattern)

    if temp == None:
        print("NO")

    else:
        print("YES")
        