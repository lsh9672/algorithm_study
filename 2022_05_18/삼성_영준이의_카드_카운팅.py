#SWEA 4047 (싸피,D3)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_18/sample_input (1).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    card_info = {"S":set(),"D":set(),"H":set(),"C":set()}

    card_input = sys.stdin.readline().strip()

    result_list = list()

    result = False

    for i in range(0,len(card_input)-2,3):

        temp = card_input[i:i+3]

        
        card_type = temp[0]

        card_num = int(temp[1:])

        if card_num in card_info[card_type]:
            result = True
            break

        else:
            card_info[card_type].add(card_num)
    
    if result == True:
        print(f"#{test_case} ERROR")

    else:
        for i in card_info.values():
            result_list.append(13-len(i))

        print(f"#{test_case}", end=" ")
        print(*result_list)

        

