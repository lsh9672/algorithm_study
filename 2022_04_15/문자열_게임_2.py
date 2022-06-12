#백준 20437번

import sys
from collections import defaultdict

t = int(sys.stdin.readline())

for _ in range(t):
    input_string = sys.stdin.readline().strip()
    k = int(sys.stdin.readline())

    string_location = defaultdict(list)

    for i in range(len(input_string)):
        string_location[input_string[i]].append(i)

    
    ##저장된 것은 있는데, k가 1이라면, 그냥 1
    if k == 1:
        print(1,1)
        continue
    
    ##3번
    min_result = 10001
    ##4번 
    max_result = 0

    for key in string_location.keys():
        temp_list = string_location[key]
        if len(temp_list) >= k:
            for i in range(len(temp_list) + 1 - k):

                temp_cal = (temp_list[i+k-1] - temp_list[i]) + 1
                ##3번 업데이트
                min_result = min(min_result,temp_cal)

                ##4번 업데이트
                max_result = max(max_result,temp_cal)

    if min_result == 10001 or max_result == 0:
        print(-1)
    else:
        print(min_result,max_result)