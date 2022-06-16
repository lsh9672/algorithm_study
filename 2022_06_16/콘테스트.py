## 백준 5576번 (스트릭 유지용)
import sys

num_list_w = list()

num_list_k = list()

for _ in range(10):
    num_list_w.append(int(sys.stdin.readline().strip()))

for _ in range(10):
    num_list_k.append(int(sys.stdin.readline().strip()))

num_list_w.sort()

num_list_k.sort()

print(f"{sum(num_list_w[7:])} {sum(num_list_k[7:])}")
