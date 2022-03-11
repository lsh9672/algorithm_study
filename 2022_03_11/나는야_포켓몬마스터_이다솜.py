#백준 1620(손풀기문제)
import sys


n,m = map(int,sys.stdin.readline().split())

#번호가 키
pocket1 = dict()

#이름이 키
pocket2 = dict()

for i in range(n):
    temp = sys.stdin.readline().strip()
    pocket1[i+1] = temp
    pocket2[temp] = i+1


result = list()
for _ in range(m):
    temp = sys.stdin.readline().strip()

    result.append(temp)

for i in result:

    if i.isalpha():
        print(pocket2[i])

    else:
        print(pocket1[int(i)])

    

