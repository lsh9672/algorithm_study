#백준 2696번 (골드2, 중앙값 구하기)
'''느린 풀이
import sys


test_case = int(sys.stdin.readline().strip())

for _ in range(test_case):

    m = int(sys.stdin.readline().strip())

    num_list = list()

    for i in range((m//10)+1):
        num_list += list(map(int,sys.stdin.readline().split()))

    # num_list.sort()

    result = list()

    for i in range(0,m,2):
        temp = num_list[:i+1]
        temp.sort()

        result.append(temp[len(temp)//2])

    print(len(result))

    for i in range(len(result)):

        if (i+1)%10 == 0:
            print(result[i], end = "\n")

        else:
            print(result[i], end = " ")
'''

'''힙을 이용한 빠른 풀이'''

import sys
import heapq


test_case = int(sys.stdin.readline().strip())

for _ in range(test_case):

    m = int(sys.stdin.readline().strip())

    num_list = list()

    for i in range((m//10)+1):
        num_list += list(map(int,sys.stdin.readline().split()))

    result = list()

    ## max heap
    left_heap = list()
    ## min heap
    right_heap = list()
    middle_value = num_list[0]
    result.append(middle_value)

    for i in range(1,len(num_list)):
        if middle_value > num_list[i]:
            heapq.heappush(left_heap,-num_list[i])
        else:
            heapq.heappush(right_heap,num_list[i])

        if i%2 == 0:
            if len(left_heap) > len(right_heap):
                heapq.heappush(right_heap,middle_value)
                middle_value = (-1) * heapq.heappop(left_heap)

            elif len(left_heap) < len(right_heap):
                heapq.heappush(left_heap, (-1)*middle_value)
                middle_value = heapq.heappop(right_heap)
            
            result.append(middle_value)

    print(len(result))

    for i in range(len(result)):

        if (i+1)%10 == 0:
            print(result[i], end = "\n")

        else:
            print(result[i], end = " ")
