#백준 11286번 (절댓값 힙)
import sys
import heapq

n = int(sys.stdin.readline())

queue = list()

result = list()

for _ in range(n):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(queue,[abs(x),x])

    else:
        if len(queue) == 0:
            print(0)

        else:
            print(heapq.heappop(queue)[1])


