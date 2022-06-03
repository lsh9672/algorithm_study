#백준 12764번 (자료구조, 골드3)
import sys
import heapq

n = int(sys.stdin.readline().strip())

## 사용자들의 시간을 저장해서 정렬함 - 시작시간이 가장 빠른사람이 먼저 입력으로 들어오지 않는 경우가 있음
pc_time_list = list()

for _ in range(n):
    pc_time_list.append(list(map(int,sys.stdin.readline().split())))

pc_time_list.sort(key = lambda x : x[0])

## 현재 사용중인 사용자들의 정보들이 들어갈 힙
use_queue = list()

## 다음 사용자가 사용할 컴퓨터 번호
computer_num = 1

##각 컴퓨터를 몇명의 사용자가 사용했는지 
result = list()

## 사용가능한 컴퓨터 번호들
useful_computer_num = list()

for start_time, end_time in pc_time_list:

    ## 큐가 비어있을 경우.
    if len(use_queue) == 0:
        heapq.heappush(use_queue,[end_time, computer_num])
        result.append(1)
        computer_num += 1

    ## 큐가 비어있지 않을 경우
    else:
        ## 큐의 peek값과 비교해서 큐의 값보다 start_time이 더 크면, pop하고 해당 pc번호에 end_time을 묶어서 큐에 넣음
        
        temp_time, temp_num = use_queue[0]

        ##여기부터 해야됨
        while temp_time <= start_time:

            useful_computer_num.append(heapq.heappop(use_queue)[1])

            if len(use_queue) != 0:
                temp_time, temp_num = use_queue[0]
            
            else:
                break
        if len(use_queue) == 0:
            useful_computer_num.sort()
            temp = useful_computer_num.pop(0)
            heapq.heappush(use_queue,[end_time,temp])
            result[temp-1] += 1
            continue
        
        if temp_time > start_time:
            ## 사용가능한 자리가 있으면
            if len(useful_computer_num) != 0:
                useful_computer_num.sort()
                temp_computer_num = useful_computer_num.pop(0)
                heapq.heappush(use_queue,[end_time,temp_computer_num])
                result[temp_computer_num-1] += 1

            ## 사용가능한 자리가 없다면
            else:
                heapq.heappush(use_queue,[end_time,computer_num])
                result.append(1)
                computer_num += 1


print(len(result))
print(*result)

