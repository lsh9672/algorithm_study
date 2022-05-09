## 백준 3018번 (실버4, 캠프파이어)
import sys

n = int(sys.stdin.readline().strip())

e = int(sys.stdin.readline().strip())

people = {node:set() for node in range(1,n+1)}

target = 0

for x in range(e):
    temp = list(map(int,sys.stdin.readline().split()))

    temp2 = set(temp[1:])
    if 1 in temp2:
        target += 1
        for i in temp2:
            people[i].add(x)
        
    else:
        for i in temp2:
            for k in temp2:
                people[k] = people[k]|people[i]

print(people)


for i in people.keys():
    if len(people[i]) == target:
        print(i)
