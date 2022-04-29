##SWEA 1244 (싸피,D3)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_04_29/input.txt", "r")

'''틀린코드 - 단순 그리디로 풀었더니 통과하지 못했다.
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    temp, change_count = sys.stdin.readline().split()

    change_count = int(change_count)

    num_value = list(temp)

    num_value = list(map(int,temp))

    count = 0

    for i in range(len(num_value)-1):
        change_target = num_value[i]

        # temp_list =  num_value[i+1:]
        temp_max_index = 0
        temp_max_value = 0
        
        for j in range(i+1,len(num_value)):
            if num_value[j] > num_value[i] and temp_max_value <= num_value[j]:
                temp_max_value = num_value[j]
                temp_max_index = j 

        if temp_max_index != 0:
            num_value[temp_max_index] = num_value[i]
            num_value[i] = temp_max_value
            count+=1

        if change_count == count:
            break


    result = "".join(list(map(str,num_value)))
        
    print(f"#{test_case} {result}")

'''

'''
구글링을 통해 참고한 풀이
dfs를 이용한 백트래킹 문제였다.
완탐을 하면 시간초과가 나니, 백트래킹으로 가지치기해서 속도를 올린 코드다
참고 글 : https://mungto.tistory.com/212

'''

def dfs(change_count:int):
    global result

    ##횟수를 다 사용했으면 숫자로 바꿔서 현재 가지고 있는 값과 비교해서 크면 갱신
    if change_count == 0:
        temp = int("".join(num_list))

        if result < temp:
            result = temp
        
        return

    ##변환횟수가 남았으면 바꿔야 됨
    for i in range(length-1):
        for j in range(i+1,length):

            ##하나씩 숫자를 정해서 바꿔봄
            num_list[i],num_list[j] = num_list[j], num_list[i]

            ##가지치기를 위해서 합쳐보고, 나왔던건지 확인함
            temp_key = "".join(num_list)

            ##여기서 get을 사용하는 이유는 []접근하는 것과 달리 값이 없더라도 예외가 터지지 않고 None리턴해줌

            ##자리를 한번 바꿨으니까 change_count를 -1해서 찾고, 1이면 아직 안나온것
            ## 두번째인자는 찾고자 하는 키가 없다면 반환해주는 디폴트값.
            ##따라서 아래의 if문이 실행되려면 키가 없어야 됨.
            if visited.get((temp_key,change_count - 1),1):

                ##언제 사용되었는지 체크해줌.
                visited[(temp_key,change_count-1)] =  0

                ##다음 경우 탐색
                dfs(change_count-1)

            
            ##다 했으면 다음 경우 탐색을 위해 바꾼수 원위치
            num_list[i],num_list[j] = num_list[j], num_list[i]


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    temp, change_count = input().split()

    num_list = list(temp)

    change_count = int(change_count)

    length = len(num_list)

    result = 0 

    ##가지치기를 위해 딕셔너리 생성
    visited = dict()

    dfs(change_count)

    print(f"#{test_case} {result}")