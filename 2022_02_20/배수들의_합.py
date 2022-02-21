#백준 17173번 - 배수들의 합 브론즈2(스트릭유지용)''
import sys

n,m = map(int, sys.stdin.readline().split())

num_list = list(map(int,sys.stdin.readline().split()))

result = [0 for _ in range(n+1)]

for i in num_list:

    temp_num = i
    #n보다 작을떄까지 반복
    while temp_num<=n:
        #만들수 있는 수 전부 리스트에 넣음
        result[temp_num] = temp_num

        #배수증가 => 2면 2씩더해서 2,4,6,8,이런식으로
        temp_num+=i

print(sum(result))