#백준 11945번 (스트릭 유지용)
import sys

n,m = map(int,sys.stdin.readline().split())

for _ in range(n):
    temp = sys.stdin.readline().strip()

    print(temp[::-1])