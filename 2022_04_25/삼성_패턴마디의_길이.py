#SWEA 2007 (싸피연습, D2)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_04_25/input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    input_string = input().strip()

    j = 0

    total_length = 0
    for i in range(1,10):
        if input_string[j] == input_string[i]:
            length = i - j
            if input_string[j:length] == input_string[length:length+length]:
                ## 그 뒤에도 반복해봄
                total_length = length
                j+=1

    
    print(f"#{test_case} {total_length}")