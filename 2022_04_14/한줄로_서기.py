#백준 1138번(구현 연습,, 실버2)
import sys

n = int(sys.stdin.readline())

num_list = list(map(int,sys.stdin.readline().split()))

result_list = [0 for _ in range(n)]

for i in range(n):
    temp = num_list[i]

    count = 0

    for j in range(n):
        if count == temp and result_list[j] == 0:
            result_list[j] = i+1
            break
        elif result_list[j] == 0:
            count += 1

print(*result_list)
