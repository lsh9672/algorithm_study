#SWEA 2930번 (싸피, D3)
import sys
import heapq

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_10/sample_input (1).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    n = int(input().strip())

    queue = list()

    result = list()

    for _ in range(n):
        temp = list(map(int,sys.stdin.readline().split()))

        if temp[0] == 1:

            heapq.heappush(queue,(-1)*temp[1])

        else:
            if len(queue) != 0:
                result.append((-1)* heapq.heappop(queue))
            else:
                result.append(-1)

    print(f"#{test_case}", end=" ")
    print(*result)