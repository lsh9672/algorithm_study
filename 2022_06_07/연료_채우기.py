#백준 1826번 (자료구조, 골드3)

'''
1202 보석도둑과 거의 같은 문제임
'''

import sys
import heapq


n = int(sys.stdin.readline().strip())

gas_station_list = list()

for _ in range(n):
    heapq.heappush(gas_station_list,list(map(int,sys.stdin.readline().split())))


##마을까지의 거리, 초기 트럭 연료
destination,fuel_num = map(int,sys.stdin.readline().split())


##시작부터 매 주유소마다, 기름을 넣고, 목적지 까지 갈수 있나 확인함
## 목적지에 갈수 없다면 현재 갈수 있는 주유소를 전부 뽑아서 선별큐에 넣음
## 선별큐에는 연료량이 가장 큰것이 첫번째로 나오도록 함.

##주유소 카운트
result = 0
selection_list = list()

current_loc = 0

##연료가 목적지보다 커질떄까지 
while destination - current_loc > fuel_num:

    while len(gas_station_list) != 0 and gas_station_list[0][0] - current_loc <= fuel_num:
        temp = heapq.heappop(gas_station_list)
        heapq.heappush(selection_list,[(-1)*temp[1],temp[0]])

    
    if len(selection_list) != 0:
        temp_fuel, temp_loc = heapq.heappop(selection_list)
        ## 현재위치에서 기름을 가장많이 채울수 있는 위치로 이동한만큼 연료 소모
        fuel_num -= temp_loc - current_loc

        ##이동후에 연료 채움
        fuel_num += (-1)*temp_fuel
        ##현재위치 갱신
        current_loc = temp_loc

        result += 1
    
    ## 현재 연료로 도달할 수 있는 주유소가 없으면, 가지고 있는 연료로 목적지에 갈 수 있는지 확인
    else:
        if destination - current_loc > fuel_num:
            result = -1
            break


print(result)