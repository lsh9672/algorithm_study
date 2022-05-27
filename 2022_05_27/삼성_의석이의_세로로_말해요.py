#SWEA 5356번 (싸피,d3)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_27/sample_input (11).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str_list = list()

    result = ""
    
    ##최대 길이 구해두기
    max_length = -1

    for _ in range(5):
        temp = sys.stdin.readline().strip()
        str_list.append(temp)

        if max_length < len(temp):
            max_length = len(temp)

    ## 최대길이보다 짧으면, 안나오는 단어("^")로 최대길이까지 채움
    for i in range(5):

        if len(str_list[i]) < max_length:
            str_list[i] += "^"*(max_length)*len(str_list[i])
    
    for i in range(max_length):
        for j in range(5):
            if str_list[j][i] != "^":
                result += str_list[j][i]


    
    print(f"#{test_case} {result}")