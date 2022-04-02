#백준 2407번 (손풀기 문제)
import sys

a,b = map(int,sys.stdin.readline().split())


    

#nCm

up = 1

for i in range(b):
    up *= (a-i)

down = 1

for j in range(b):
    down *= j+1

print(up//down)