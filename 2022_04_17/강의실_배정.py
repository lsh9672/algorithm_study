#백준 11000 (자료구조, 골드5)

'''알게된 점'''
#힙에서 뺴고 새로운 값을 넣을때, pop,push를 각각하지 않고, heapreplace를 쓰면 한번에 해결된다.
#단, 속도가 더 빠르거나 하지는 않음

import sys
import heapq

n = int(sys.stdin.readline())

class_list = list()

classroom_list = list()

for _ in range(n):
    class_list.append(list(map(int,sys.stdin.readline().split())))

#시작시간이 빠른게 앞으로 오도록 변경
class_list.sort()

## 첫번쨰는 바로 힙으로 넣음 - 강의가 끝나는 시간을 넣음
## 끝나는 시간을 넣어야 다음 강의의 시작 시간과 비교해서 회의실을 추가할지 기존것을 쓸지 판단가능

heapq.heappush(classroom_list,class_list[0][1])

for i in range(1,n):
    ## 힙에서 다음에 뺄 원소와, 다음 수업의 시작시간을 비교해봄
    
    ## 첫번쨰 원소와 다음 수업의 시작시간을 비교했을떄,  힙의 원소가 더 크면, 회의실을 추가해야됨
    if classroom_list[0] > class_list[i][0]:
        heapq.heappush(classroom_list,class_list[i][1])

    ## 힙의 원소가 더 작거나 같으면, 강의실 추가 없이 그대로 사용
    else:
        # heapq.heappop(classroom_list)
        # heapq.heappush(classroom_list,class_list[i][1])
        heapq.heapreplace(classroom_list,class_list[i][1])

print(len(classroom_list))

