#백준 9375번 (자료구조 연습)
import sys
from collections import defaultdict


test_case = int(sys.stdin.readline())

for _ in range(test_case):

    n = int(sys.stdin.readline())

    wear_dict = defaultdict(list)

    for _ in range(n):
        a,b = map(str,sys.stdin.readline().split())

        wear_dict[b].append(a)


    temp = wear_dict.keys()

    total = 1
    for i in temp:
        total *= len(wear_dict[i])+1
    
    print(total-1)