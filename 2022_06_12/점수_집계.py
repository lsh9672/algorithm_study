#백준 9076번 (브론즈, 스트릭유지용)
import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    num_list = list(map(int,sys.stdin.readline().split()))
    num_list.sort()

    num_list = num_list[1:len(num_list)-1]

    if num_list[-1] - num_list[0] >= 4:
        print("KIN")

    else:
        print(sum(num_list))