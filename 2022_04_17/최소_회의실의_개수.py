#백준 19598번 (자료구조 연습, 골드5)
import sys
import heapq


n = int(sys.stdin.readline())

meeting_list = list()

meeting_room_list = list()

for _ in range(n):
    meeting_list.append(list(map(int,sys.stdin.readline().split())))

## 시작시간 순으로 정렬
meeting_list.sort()

## 첫번째 값 힙에 넣기
heapq.heappush(meeting_room_list,meeting_list[0][1])

for i in range(1,n):

    if meeting_room_list[0] > meeting_list[i][0]:
        heapq.heappush(meeting_room_list,meeting_list[i][1])
    
    else:
        heapq.heapreplace(meeting_room_list,meeting_list[i][1])

print(len(meeting_room_list))

