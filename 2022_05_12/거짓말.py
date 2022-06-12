#백준 1043번 (골드4, 자료구조 및 그래프 탐색)
import sys

n, m = map(int,sys.stdin.readline().split())

##진실을아는 사람
temp_num = list(map(int,sys.stdin.readline().split()))

true_people = set(temp_num[1:])


party_list = list()

for _ in range(m):
    temp = list(map(int,sys.stdin.readline().split()))

    party_list.append(temp[1:])

for _ in range(m):
    ##파티에 진실을 아는 사람이 있으면 나머지도 전부 진실을 알아야됨.
    for i in party_list:
        if true_people & set(i):
            true_people = true_people | set(i)


## 진실을 아는 사람이 없으면 전부 과장되게 말해도됨
if len(true_people) == 0:
    print(m)

##진실을 아는 사람이 있으면 확인.
else:
    result = 0
    for party in party_list:
        
        if set(party)&true_people:
            continue
            
        result += 1

    print(result)








