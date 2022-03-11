#백준 11651번 (좌표정렬하기2)
import sys

test_case = int(sys.stdin.readline())

num_list = list()

for _ in range(test_case):
    num_list.append(list(map(int,sys.stdin.readline().split())))


num_list.sort(key = lambda x: (x[1],x[0]))

for a,b in num_list:
    print(a,b)