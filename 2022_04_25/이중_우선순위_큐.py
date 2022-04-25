#백준 7662번 (자료구조 골드4)
import sys
import heapq
from collections import defaultdict


test_case = int(sys.stdin.readline())

result = list()

for _ in range(test_case):
    operator_num = int(sys.stdin.readline().strip())

    min_heap = list()

    max_heap = list()

    ##해시충돌을 생각해서 set을 썼는데, 중복되는 데이터처리 불가능해짐
    ##따라서 딕셔너리를 써야됨
    temp_min = defaultdict(int)
    temp_max = defaultdict(int)

    for _ in range(operator_num):
        
        command, value = sys.stdin.readline().strip().split()

        value =int(value)

        # print(f"max heap : {max_heap}, min heap : {min_heap}")

        if command == "I":
            heapq.heappush(min_heap,value)
            heapq.heappush(max_heap,value*(-1))

        
        elif command == "D":
            if value == 1:
                
                if len(max_heap) == 0:
                    continue
                    
                temp = (-1) * heapq.heappop(max_heap)
                check = True
                ## 힙이 비지 않았고, 반대쪽 큐에 있다면 반복 
                while (temp in temp_min) and temp_min[temp] > 0:
                    temp_min[temp] -= 1 
                    if len(max_heap) == 0:
                        check = False
                        break

                    temp = (-1) * heapq.heappop(max_heap)

                ##최종적으로 나온 값 dic에 넣어두기
                if check == True:
                    temp_max[temp]+=1

            elif value == -1:
                if len(min_heap) == 0:
                    continue
                    
                temp = heapq.heappop(min_heap)
                check = True
                ## 힙이 비지 않았고, 반대쪽 큐에 있다면 반복 
                while (temp in temp_max) and temp_max[temp] > 0:
                    temp_max[temp] -= 1 
                    if len(min_heap) == 0:
                        check = False
                        break

                    temp = heapq.heappop(min_heap)
                
                ##최종적으로 나온 값 dic에 넣어두기
                if check == True:
                    temp_min[temp]+=1

    if len(max_heap) == 0 or len(min_heap) == 0:
        print("EMPTY")

    else:
        # print(f"max_heap : {max_heap}, min_heap : {min_heap}")
        # print(f"temp_max : {temp_max}, temp_min : {temp_min}")
        while len(max_heap) != 0 and ((-1)*max_heap[0]) in temp_min and temp_min[(-1)*max_heap[0]]>0:

            temp_min[(-1)*heapq.heappop(max_heap)] -=1


        while len(min_heap) != 0 and (min_heap[0] in temp_max) and temp_max[min_heap[0]]>0:
            temp_max[heapq.heappop(min_heap)] -=1
        # print(f"max_heap : {max_heap}, min_heap : {min_heap}")
        # print(f"temp_max : {temp_max}, temp_min : {temp_min}")
        if len(max_heap) == 0 or len(min_heap) == 0:
            print("EMPTY")
        else:
            print((-1)*max_heap[0], min_heap[0]) 

    
