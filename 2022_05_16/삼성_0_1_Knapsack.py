#SWEA 3282 (싸피,d3)

import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_16/sample_input (9).txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0
    
    num_item, bag_size = map(int,sys.stdin.readline().split())

    size_list = list()
    value_list = list()

    for _ in range(num_item):
        temp_size, temp_value = map(int,sys.stdin.readline().split())

        size_list.append(temp_size)
        value_list.append(temp_value)

    dp = [[0 for _ in range(bag_size+1)] for _ in range(num_item+1)]

    for i in range(1,num_item+1):
        for j in range(1,bag_size+1):
            
            #물건의 부피가 가방의 부피보다 크면
            if size_list[i-1] > j:
                ## 업데이트 없이 이전값 그냥 가져오기
                dp[i][j] = dp[i-1][j]

            else:
                dp[i][j] = max(value_list[i-1]+dp[i-1][j-size_list[i-1]], dp[i-1][j])
    
    result = dp[num_item][bag_size]
    print(f"#{test_case} {result}")