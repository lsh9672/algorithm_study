#SWEA 3456번 (싸피,D3)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_17/sample_input (12).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다. 
for test_case in range(1, T + 1):

    a,b,c = map(int,sys.stdin.readline().split())
    
    temp_hap = a+b+c

    temp_set = set([a,b,c])

    result = 0

    if len(temp_set) == 1:
        result = a

    else:
        temp_total = 0
        for i in temp_set:
            temp_total += i*2

        result = temp_total - temp_hap    


    print(f"#{test_case} {result}")
    
