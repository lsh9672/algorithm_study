#백준 25238번 (스프릭 유지용)
import sys

a,b = map(int,sys.stdin.readline().split())

temp = a - (a*b) / 100

if temp > 100:
    print(0)

else:
    print(1)