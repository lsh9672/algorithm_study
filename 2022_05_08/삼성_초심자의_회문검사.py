#SWEA 1989번 (싸피,D2)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_08/input (20).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0
    
    input_str = sys.stdin.readline().strip()

    if input_str == input_str[::-1]:
        result = 1


    print(f"#{test_case} {result}")