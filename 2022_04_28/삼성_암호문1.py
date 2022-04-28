#SWEA 1228번(싸피대비 D3)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_04_28/input (13).txt", "r")
# sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_04_28/test.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1,11): 

    n = int(input())

    origin_secret = list(map(int,input().split()))

    command_num = int(input().strip())

    commands = input().split()
    
    index = 0

    while index < len(commands):
        x = int(commands[index + 1])
        y = int(commands[index+2])
        s = list(map(int,commands[index+3:index+3+y]))

        for i in range(y-1,-1,-1):
            origin_secret.insert(x,s[i])


        index += y+3
        

    result = origin_secret[:10]


    print(f"#{test_case}", end=" ")
    print(*result)


