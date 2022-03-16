#백준 11659번 구간합구하기4(누적합)
import sys

n,m = map(int,sys.stdin.readline().split())

num_list = list(map(int,sys.stdin.readline().split()))

#누적합 리스트 - 기존 리스트 누적합으로 만들기
for i in range(n-1):
    num_list[i+1] += num_list[i]

print(num_list)
result = list()
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())

    a = a-1
    b = b-1
    if a<=0:
        result.append(num_list[b])
    else:
        result.append(num_list[b] - num_list[a-1])
        
    # print(num_list[b-1] - num_list[a-2])
    

for i in result:
    print(i)

#누적합 없이 순수 반복문으로  - 시간초과
# def find_func(a:list,b:list):
#     total = 0
#     for i in range(a,b+1):
#         total += num_list[i]

#     return total

# for _ in range(m):
#     a,b = map(int,sys.stdin.readline().split())
#     print(find_func(a-1,b-1))
