#백준 10816번 (자료구조, 실버4)
import sys

n = int(sys.stdin.readline())

card_num = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())

find_num = list(map(int,sys.stdin.readline().split()))

result =[0] * m

num_dict = dict()

for i in card_num:

    if i in num_dict:
        num_dict[i] += 1

    elif i not in num_dict:
        num_dict[i] = 1


for j in range(m):

    if find_num[j] in num_dict:

        result[j] = num_dict[find_num[j]]

print(*result)




