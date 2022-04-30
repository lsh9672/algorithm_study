## 백준 17219번 (자료구조 연습, 실버4)

import sys

n,m = map(int,sys.stdin.readline().split())

site_dict = {}

for _ in range(n):

    name,passwd = sys.stdin.readline().split()

    site_dict[name] = passwd


for _ in range(m):
    print(site_dict[sys.stdin.readline().strip()])

