#병합 정렬 구현
import random

#리스트 절반으로 나누는 함수
def merge_split(data_list:list) -> list:
    if len(data_list) <= 1:
        return data_list
    
    medium = len(data_list) // 2
    left_list = merge_split(data_list[:medium])
    right_list = merge_split(data_list[medium:])

    return merge(left_list,right_list)


def merge(left_list:list,right_list:list) -> list:
    temp_merge_list = list()
    left_point,right_point = 0,0

    #case1 - left/right 둘다 있을때
    while len(left_list) > left_point and len(right_list) > right_point:
        if left_list[left_point] > right_list[right_point]:
            temp_merge_list.append(right_list[right_point])
            right_point += 1

        else:
            temp_merge_list.append(left_list[left_point])
            left_point += 1

    #case2 - left 데이터가 없을경우
    while len(left_list) > left_point:
        temp_merge_list.append(left_list[left_point])
        left_point += 1

    #case3 - right - 데이터가 없을 경우
    while len(right_list) > right_point:
        temp_merge_list.append(right_list[right_point])
        right_point += 1

    return temp_merge_list



if __name__ == "__main__":
    test_list = random.sample(range(100),15)

    print(test_list)
    print(merge_split(test_list))
