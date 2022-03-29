#백준 1254번 (문자열 연습, 실버1)

import sys

s = sys.stdin.readline().strip()

for i in range(len(s)):
    temp = s[i:]
    if temp == temp[::-1]:
        print(len(s)+i)
        break
