#백준 2108번 (정렬 연습 실버3)
import sys


n = int(sys.stdin.readline())

num_list = list()

for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

## 산술평균
print(round(sum(num_list)/n))

##중앙값
num_list.sort()
print(num_list[(n-1)//2])

##최빈값
num_dict = dict()
for i in num_list:
    if i in num_dict:
        num_dict[i] += 1
    
    else:
        num_dict[i] = 1

temp_list = sorted(list(num_dict.items()), key= lambda x: x[1])

temp = list()

for i in temp_list:
    if i[1] == temp_list[-1][1]:
        temp.append(i[0])

temp.sort()

if len(temp) > 2:
    print(temp[1])

elif len(temp) == 2:
    print(temp[1])

else:
    print(temp[0])

##범위
print(num_list[-1] - num_list[0])