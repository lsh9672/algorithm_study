#백준 2346번(실버3, 자료구조연습)

'''파이썬 deque에는 로테이트라는 아주 좋은 기능을 제공함.'''
import sys
from collections import deque

n = int(sys.stdin.readline())

temp = list(map(int,sys.stdin.readline().split()))

balloon_list = deque(list())

result = []

for index,value in enumerate(temp):
    balloon_list.append([index,value])

while balloon_list:
    current_index,current_value = balloon_list.popleft()
    result.append(str(current_index+1))

    #주어진 숫자대로 회전하면 틀림 - 리스트 안의 수는 계속 pop되어서 줄어들기 때문에 주어진 숫자가 이동할 방향의 반대로 돌려야됨
    if current_value >0:
        balloon_list.rotate(current_value *(-1) + 1)

    elif current_value < 0:
        balloon_list.rotate(current_value *(-1))

    

print(" ".join(result))

