#SWEA 1217번 (싸피 대비 D3)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_04_25/input (7).txt", "r")


def recursive(num:int,count:int,num_count):
    if count > num_count:
        return 1
    else:

        return num * recursive(num,count+1,num_count)


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for _ in range(1, 11):
    
    test_case = int(input())

    num, num_count = map(int,input().split())

    result = recursive(num,1,num_count)

    print(f"#{test_case} {result}")



