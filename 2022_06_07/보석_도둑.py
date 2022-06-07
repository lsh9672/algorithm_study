#백준 1202번 (자료구조, 골드2)
import sys
import heapq

n,k = map(int,sys.stdin.readline().split())

##보석 저장
jewel_list = list()

## 보석 무게, 가격으로 묶어서 힙에 넣음
for _ in range(n):
    heapq.heappush(jewel_list,list(map(int,sys.stdin.readline().split())))

bag_weight = list()

for _ in range(k):
    bag_weight.append(int(sys.stdin.readline().strip()))

##오름차순 정렬
bag_weight.sort()


result = 0 

## 선별한 보석들의 무게를 담는 우선순위 큐
selection_list = list()

## 작은 가방부터 하나씩 꺼내서 해당 무게를 넘어가지 않는것들을 선별해서 힙에 넣는다.
## 작은 무게부터 하는 이유는 작은무게를 만족하면, 그것보다 큰 것들은 다 만족하기 떄문
## 큰 무게 부터 내려가면, 작은 무게에서 넣지 못하는 것이 선별될수도 있음 - 즉 최대가격을 만들지 못할수 있음
for weight in bag_weight:
    
    ##현재 무게보다 작거나 같으면 꺼내서 별도의 힙에 계속 넣어둠
    while len(jewel_list) != 0 and weight >= jewel_list[0][0]:
        temp_jewel = heapq.heappop(jewel_list)
        heapq.heappush(selection_list,(-1) * temp_jewel[1])

    
    if len(selection_list) != 0:
        result += (-1)*heapq.heappop(selection_list)
        

print(result)