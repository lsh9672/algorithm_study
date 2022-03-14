#백준  1021번 자료구조 연습(덱)
import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

wanted_num = list(map(int,sys.stdin.readline().split()))

num_list = deque([i+1 for i in range(n)])


operation_count = 0

for i in wanted_num:

    #큐의 첫번째 값이 뽑아야될 값(i)이면 명령어1번 실행
    if num_list[0] == i:
        num_list.popleft()

    
    #첫번째 값이 뽑아야될 값이 아니라면 반복해서 2,3번을 실행함.
    else:
        #현재 인덱스 위치에서 오른쪽,왼쪽중, 어디로 가는게 더 빠른지 계산.
        
        right = len(num_list) - num_list.index(i)
        left = num_list.index(i)

        #뽑아야되는 값 기준으로 오른쪽 보다 왼쪽이 더 짧으면 왼쪽으로 회전
        if left < right:
            num_list.rotate(left *(-1))
            operation_count += left

        else:
            num_list.rotate(right)
            operation_count += right
        
        num_list.popleft()

print(operation_count)
