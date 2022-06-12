#백준 7568번 실버5

import sys


test_case = int(sys.stdin.readline())

info_list = list()

#리스트에 모든 정보들 넣기
for _ in range(test_case):
    x,y = map(int,sys.stdin.readline().split())

    info_list.append([x,y,0])

for i in range(test_case):
    main_people = info_list[i]
    count = 0

    for j in range(test_case):

        sub_people = info_list[j]

        if i==j:
            continue
            
        #나보다 큰사람
        if main_people[0] < sub_people[0] and main_people[1] < sub_people[1]:
            count+=1

    info_list[i][2] = count+1
        
for i in range(test_case):

    print(info_list[i][2],end=" ")



