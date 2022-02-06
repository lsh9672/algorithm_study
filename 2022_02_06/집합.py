#백준 알고리즘 11723 - 집합

import sys

#수행할 연산수
m = int(sys.stdin.readline())

#비어있는 공집합
s = set()

for _ in range(m):
    temp = sys.stdin.readline().split()
    
    #all 일때
    if temp[0] == 'all':
        #시간 줄일라면 for 쓰면 안됨
        s = set(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
    #empty 일때
    if temp[0]== 'empty':
        #초기화
        s = set()
    #add 일때
    if temp[0] == 'add':
        s.add(temp[1])
    #remove 일때
    if temp[0] == 'remove':
        s.discard(temp[1])
    #check 일때
    if temp[0] == 'check':
        #값이 있으면 1
        if temp[1] in s:
            sys.stdout.write('1\n')
        #없으면 0
        else:
            sys.stdout.write('0\n')
    #toggle 일때
    if temp[0] == 'toggle':
        #있으면 삭제
        if temp[1] in s:
            s.discard(temp[1])
        #없으면 추가
        else:
            s.add(temp[1])
