#백준 1927번(자료구조 연습)
import sys
import heapq

n = int(sys.stdin.readline())

queue = []

for _ in range(n):

    temp = int(sys.stdin.readline())

    if temp == 0:
        #큐가 비어있으면, 0
        if len(queue) == 0:
            print(0)

        else:
            print(heapq.heappop(queue))

    else:
        heapq.heappush(queue,temp)

    
