import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_04_26/input.txt", "r")


def palindrome(input_string:str)->bool:
    start = 0 
    end = len(input_string) - 1

    while start < end:

        if input_string[start] == input_string[end]:
            start += 1
            end -= 1
        
        else:
            return False
    
    return True


def palindrome_num(field:list,n)-> int:

    result = 0
    #각 행별 회문 구하기
    for i in range(8):
        for j in range(len(field[0])-n+1):
            if palindrome(field[i][j:j+n]) == True:
                result += 1

    return result
    

##배열 회전
def rotation(field:list)->list:
    temp = [[0 for _ in range(len(field))] for _ in range(len(field[0]))]

    for i in range(len(field)):
        for j in range(len(field[0])):
            temp[j][i] = field[i][j]

    return temp


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1,11):
    n = int(input())

    field = list()

    for _ in range(8):
        field.append(sys.stdin.readline().strip())
    
    result = 0

    ##행별
    result += palindrome_num(field,n)

    ##슬라이싱을 위해 배열 회전
    field = rotation(field)

    ##열별
    result += palindrome_num(field,n)


    print(f"#{test_case} {result}")