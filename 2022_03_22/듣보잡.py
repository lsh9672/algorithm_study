#백준 1764번 (실버4, 자료구조)
import sys

n,m = map(int,sys.stdin.readline().split())

not_see_man = dict()

not_listen_man = dict()

for _ in range(n):
    temp = sys.stdin.readline().strip()

    not_see_man[temp] = 1


for _ in range(m):
    temp = sys.stdin.readline().strip()

    not_listen_man[temp] = 1

result = list()

for i in not_see_man.keys():

    if i in not_listen_man:
        result.append(i)

result.sort()

print(len(result))
for i in result:
    print(i)