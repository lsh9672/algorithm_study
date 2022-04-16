#백준 17140번
import sys


#x,y좌표, 값
r,c,k = map(int,sys.stdin.readline().split())

array_a = list()

for _ in range(3):
    array_a.append(list(map(int,sys.stdin.readline().split())))

print(array_a)
