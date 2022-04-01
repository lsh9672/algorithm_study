#백준 11478번 (파이썬 문자열 연습)
import sys


s = sys.stdin.readline().strip()

result = set()

for i in range(len(s)):
    for j in range(i,len(s)):

        result.add(s[i:j+1])

print(len(result))