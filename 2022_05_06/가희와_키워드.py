#백준 22233번 (자료구조 연습, 실버2)
import sys

n,m = map(int,sys.stdin.readline().split())

memo_set = set()

for _ in range(n):
    temp = sys.stdin.readline().strip()

    memo_set.add(temp)

for _ in range(m):
    temp_list = list(sys.stdin.readline().strip().split(","))

    for i in temp_list:
        if i in memo_set:
            memo_set.discard(i)

    print(len(memo_set))