#백준 21944번 (자료구조 연습,골드3)
import sys

## 문제번호: P, 난이도:L, 알고리즘 분류: G
n = int(sys.stdin.readline())

num_list = list()

for _ in range(n):

    num_list.append(tuple(map(int,sys.stdin.readline().split())))

print(num_list)
