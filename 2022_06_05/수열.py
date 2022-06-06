#백준 2491번 (디피, 실버4)

''' 아이디어
증가하는 최장수열과, 감소하는 최장 수열을 구하는 리스트를 각각 구해서 둘중 가장 큰 값을 출력한다.
'''

import sys


n = int(sys.stdin.readline().strip())

num_list = list(map(int,sys.stdin.readline().split()))


ascending_list = [1 for _ in range(n)]

descending_list = [1 for _ in range(n)]

for i in range(1,n):

    ##오름차순
    if num_list[i-1] <= num_list[i]:
        ascending_list[i] = ascending_list[i-1] + 1

    ##내림차순
    if num_list[i-1] >= num_list[i]:
        descending_list[i] = descending_list[i-1]+1

ascending_max = max(ascending_list)
descending_max = max(descending_list)

print(max(ascending_max,descending_max))
