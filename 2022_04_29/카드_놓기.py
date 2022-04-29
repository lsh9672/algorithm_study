#백준 18115번 (자료구조 연습, 실버3)
import sys
from collections import deque

n = int(sys.stdin.readline())

card_list = list(map(int,sys.stdin.readline().split()))

result = deque()

for i in range(n):
    if card_list[n-1-i] == 1:
        result.appendleft(i+1)
    
    elif card_list[n-1-i] == 2:
        result.insert(1,i+1)

    elif card_list[n-1-i] == 3:
        result.append(i+1)

print(*result)

