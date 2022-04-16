#백준 2217번 (손풀기 겸 스트릭 유지)
import sys

n = int(sys.stdin.readline())

num_list = list()

for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()

for i in range(n):
    num_list[i] = num_list[i] * (n-i)

print(num_list)

print(max(num_list))