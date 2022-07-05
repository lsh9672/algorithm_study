import sys
from itertools import permutations

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_07_05/input (8).txt", "r")

max_value = float("inf")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(sys.stdin.readline().strip())

    input_info = list(map(int,sys.stdin.readline().split()))

    start_node = [input_info[0],input_info[1]]

    end_node = [input_info[2],input_info[3]]

    people_loc = list()
    
    result = max_value

    for i in range(0,n*2,2):
        people_loc.append(input_info[4+i:6+i])

    

    for temp in permutations(people_loc, n):

        temp = list(temp)
        temp = [start_node] + temp + [end_node]

        temp_total = 0

        for i in range(n+1):
            start_loc = temp[i]
            end_loc = temp[i+1]

            temp_total += abs(start_loc[0] - end_loc[0]) + abs(start_loc[1] - end_loc[1])

        result = min(result,temp_total)

    print(f"#{test_case} {result}")