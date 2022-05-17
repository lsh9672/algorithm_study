#SWEA 3408번 (싸피, D3)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_17/sample_input (10).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    n = int(sys.stdin.readline().strip())

    s1 = n * (n+1) // 2
    s2 = n * (n+1) - n
    s3 = n * (n+1)


    print(f"#{test_case} {s1} {s2} {s3}")