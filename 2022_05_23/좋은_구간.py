#백준 1059번 (구현, 실버5)
import sys

l = int(sys.stdin.readline().strip())

s = list(map(int,sys.stdin.readline().split()))

n = int(sys.stdin.readline().strip())

s.sort()


for i in range(l):
    if s[i] == n:
        print(0)
        break
    
    elif s[i] > n:

        total = s[i] - n -1

        start = 0
        if i == 0:
            start = 1
        else:
            start = s[i-1]+1
            
        for j in range(start,n):
            total += s[i] - n

        print(total)
        break