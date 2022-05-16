# 백준 2559번 (누적합, 투포인터, 실버3)
import sys


n,k = map(int,sys.stdin.readline().split())

temp = list(map(int,sys.stdin.readline().split()))

## 구간합 계산을 위해 누적합을 계산한 리스트
num_list = [0 for _ in range(n)]

num_list[0] = temp[0]

for i in range(1,n):

    num_list[i] = num_list[i-1] + temp[i]

start_index = 0
end_index = k

result = num_list[k-1]

while end_index < n:

    result = max(result,num_list[end_index] - num_list[start_index])

    start_index += 1

    end_index = start_index + k
print(result)