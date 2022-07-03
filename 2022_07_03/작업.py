##백준 2056번 (위상정렬, 골드5)
import sys
from collections import deque

n = int(sys.stdin.readline().strip())


##선행작업들을 저장함.
graph = [list() for _ in range(n+1)]

##작업에 걸리는 시간
work_time_list = [0 for _ in range(n+1)]

for i in range(1,n+1):
    temp = list(map(int,sys.stdin.readline().split()))

    work_time_list[i] = temp[0]
    
    if temp[1] > 0:
        for j in temp[2:]:
            graph[i].append(j)

for i in range(1,n+1):
    if len(graph[i]) != 0:
        temp_time = 0

        for j in graph[i]:
            temp_time = max(temp_time,work_time_list[j])

        work_time_list[i] += temp_time
print(max(work_time_list))
        

