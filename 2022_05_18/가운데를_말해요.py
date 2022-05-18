#백준 1655번 (골드2, 자료구조)

import sys
import heapq

##정수의 개수
n = int(sys.stdin.readline().strip())

##중앙값보다 작은 값을 저장하는 최대 힙
left_queue = list()

##중앙값보다 큰 값을 저장하는 최소 힙
right_queue = list()

middle_value = int(sys.stdin.readline().strip())

result = list()
result.append(middle_value)


for i in range(1,n):
    temp_num = int(sys.stdin.readline().strip())

    if middle_value > temp_num:
        heapq.heappush(left_queue,(-1)*temp_num)

    else:
        heapq.heappush(right_queue, temp_num)

    ## i가 짝수 일떄, 왼쪽과 오른쪽힙의 길이를 비교해서 두 길이를 같게 만들고나서 중앙값을 저장함.
    if i%2 == 0:

        if len(left_queue) > len(right_queue):
            heapq.heappush(right_queue,middle_value)
            middle_value = (-1) * heapq.heappop(left_queue)

        elif len(left_queue) < len(right_queue):
            heapq.heappush(left_queue,(-1) * middle_value)
            middle_value = heapq.heappop(right_queue)
        
        result.append(middle_value)

    ## 홀수일떄 - 입력받은 값과 현재 중앙값을 비교해서 작은 값을 출력함
    else:
        if len(left_queue) > len(right_queue):
            heapq.heappush(right_queue,middle_value)
            middle_value = (-1) * heapq.heappop(left_queue)

        result.append(middle_value)

for i in result:
    print(i)
    
