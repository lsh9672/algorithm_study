#SWEA 1216번 (싸피대비,D3)

import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_04_26/input (9).txt", "r")


def palindrome_check(input_string:str)->bool:
    if input_string == input_string[::-1]:
        return len(input_string)

    return -1

def rotation_field(field:list)->list:
    temp = [[0 for _ in range(len(field))] for _ in range(len(field[0]))]

    for i in range(len(field)):
        for j in range(len(field[0])):
            temp[j][i] = field[i][j]

    return temp

def palindrome(field:list,result:int)->int:
    for i in range(len(field)):
        for j in range(len(field[0])):
            for k in range(len(field[0])-1,j-1,-1):
                
                if field[i][j] == field[i][k]:
                    temp = palindrome_check(field[i][j:k+1]) 
                    if temp != -1:
                        result = max(result,temp)
                        break

    return result

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):

    n = int(input())

    field = list()

    for _ in range(100):
        field.append(input().strip())

    ## 행
    result = palindrome(field,0)


    field = rotation_field(field)

    ##열
    result = palindrome(field,result)



    print(f"#{test_case} {result}")
    