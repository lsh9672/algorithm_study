#백준 2109번 (골드3, 자료구조)
import sys
import heapq

n = int(sys.stdin.readline().strip())

lecture_list = list()
queue = list()


for _ in range(n):
    lecture_list.append(list(map(int,sys.stdin.readline().split())))

lecture_list.sort(key=lambda x : x[1])

for i in lecture_list:
    ##힙에 강연료를 넣을껀데, 넣고, 해당 강의시간과, 리스트 길이를 비교해서 리스트 길이가 더 길다면, 처리할 수 없는 강의가 있다는 뜻으로, pop함
    ## 최소힙이므로 pop하면 강연료가 가장 적은 것이 빠짐.
    heapq.heappush(queue, i[0])

    if len(queue) > i[1]:
        heapq.heappop(queue)

print(sum(queue))


