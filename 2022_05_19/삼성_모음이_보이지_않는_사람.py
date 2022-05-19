##SWEA 4406번 (싸피,D3)
import sys


sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_19/1_input_sample.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

vowel_set = {"a","e","i","o","u"}

for test_case in range(1, T + 1):
    
    input_string = sys.stdin.readline().strip()

    result = ""

    for i in input_string:
        if i not in vowel_set:
            result += i
    

    print(f"#{test_case} {result}")