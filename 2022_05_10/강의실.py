#백준 1374번 (자료구조, 골드5)
import sys
import heapq


n = int(sys.stdin.readline().strip())

lec_list = list()

lecture_count = 0

for _ in range(n):

    lec_num, start_time, end_time = map(int,sys.stdin.readline().split())

    lec_list.append([start_time,end_time,lec_num])

lec_list.sort()

queue = list()

for temp_start,temp_end, temp_num in lec_list:

    if len(queue) == 0:
        heapq.heappush(queue,temp_end)
        lecture_count += 1

    else:
        if queue[0] <= temp_start:
            heapq.heappop(queue)
            heapq.heappush(queue,temp_end)

        else:
            heapq.heappush(queue,temp_end)
            lecture_count += 1

print(lecture_count)



