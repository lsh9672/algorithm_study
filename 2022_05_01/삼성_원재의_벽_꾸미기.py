#SWEA 1491번(싸피대비, D3)
import sys
## A X lR – Cl + B X (N - R X C)

# sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_01/input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n,a,b = map(int,sys.stdin.readline().split())

    ##1,1일떄 넣기
    result = b*(n-1)
    
    for i in range(1,n+1):

        j = 1
        while i*j <= n:
            temp = a* abs(i-j) + b*(n-(i*j))

            result = min(temp,result)

            j+=1

    print(f"#{test_case} {result}")