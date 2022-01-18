#퀵 소트 구현
import random

def quick_sort(data_list:list) -> list:
    #나열된 리스트의 크기가 1이면 정렬할 필요없음
    if len(data_list) <= 1:
        return data_list
    
    #왼쪽에 넣을 리스트, 오른쪽에 넣을 리스트 만들기
    left_list, right_list = list(),list()
    #기준점 변수 - 첫번째 값으로 잡음
    pivot = data_list[0]

    #크기에 따라 왼쪽 오른쪽으로 나열
    for i in range(1,len(data_list)):
        if pivot > data_list[i]:
            left_list.append(data_list[i])

        else:
            right_list.append(data_list[i])

    return quick_sort(left_list)+[pivot]+quick_sort(right_list)


if __name__ == "__main__":
    test_list = random.sample(range(100),15)
    print(test_list)
    print(quick_sort(test_list))