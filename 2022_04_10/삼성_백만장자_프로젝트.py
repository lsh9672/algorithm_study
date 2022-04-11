#swea - d2
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_04_10/input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n = int(input())

    num_list = list(map(int, input().split()))

    result = 0
    
    while num_list:
        max_value = max(num_list)

        max_value_index = num_list.index(max_value)

        temp_money = 0
        for i in range(max_value_index):
            temp_money += num_list[i]
        
        result += (max_value_index * max_value) - temp_money


        num_list = num_list[max_value_index+1:]
    

    print(f"#{test_case} {result}")
    


        

