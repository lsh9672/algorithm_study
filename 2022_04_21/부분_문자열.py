#백준 16916번 (문자열,골드3)
import sys

s = sys.stdin.readline().strip()

p = sys.stdin.readline().strip()


if p in s:
    print(1)

else:
    print(0)