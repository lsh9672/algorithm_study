#백준 11279번 (최대힙, 자료구조 연습)
import sys
import heapq

n = int(sys.stdin.readline())

heap_list = list()

result = list()

for _ in range(n):

    temp = int(sys.stdin.readline())

    if temp == 0:
        if len(heap_list) == 0:
            # print(0)
            result.append(0)
        else:
            # print(heapq.heappop(heap_list))
            result.append((-1)*heapq.heappop(heap_list))

    else:
        heapq.heappush(heap_list,temp*(-1))

for i in result:
    print(i)
