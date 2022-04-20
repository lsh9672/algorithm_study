#백준 5430번 (골드5, 자료구조)
import sys
from collections import deque

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    commands = sys.stdin.readline().strip()

    n = int(sys.stdin.readline())  

    ## 배열이 문자열로 들어와서 이를 파싱
    temp = sys.stdin.readline().strip()[1:-1]

    result_check = True

    num_list = list()

    ## 빈 배열이 아니면
    if len(temp) != 0:
        num_list = list(map(str, temp.split(",")))
    
    ## 배열을 앞에서 빼기 용이하게 큐로 바꿈
    num_list = deque(num_list)

    ## 연산
    reverse_count = 0
    for command in commands:
        ##R이면 문자열 뒤집는 카운트
        if command == "R":
            reverse_count += 1
            result_check = True

        ##D이면 두가지 경우를 확인해야됨
        elif command == "D":
            ## 배열이 비었다면 에러
            if len(num_list) == 0:
                result_check = False
            
            ##안비었으면 배열카운트 확인하고 앞에서 뻄
            else:
                if reverse_count % 2 == 1:
                    # 뒤집어야되는 경우면 뒤에서 뺴면 됨
                    num_list.pop()
                    
                else:
                    num_list.popleft()
                    reverse_count = 0
                    
                    
                result_check = True
    
    if result_check == False:
        print("error")

    else:
        if reverse_count % 2 == 1:
            num_list.reverse()
            print("[" + ",".join(num_list).strip() + "]")
        else:
            print("[" + ",".join(num_list).strip() + "]")
