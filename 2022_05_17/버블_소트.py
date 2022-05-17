#백준 1517번 (버블 소트, 플래티넘5)

'''
아이디어
- 문제에서는 버블 소트라고 되어있지만, 버블소트는 O(n^2)이다
주어지는 데이터의 최대수는 500,000 즉, 최악의 경우 250,000,000,000 (2천5백억) 번 연산을 해야된다.
따라서 이 문제는 병합정렬로 풀어야 한다.
즉, 분할정복을 해야 한다
이렇게 생각한 이유는 버블소트의 경우에는, 리스트의 길이 만큼 진행했을때 완전하게 정렬이 안되기 떄문에, 최대 리스트의 길이만큼 또 반복해야 된다
그래서 n^2이 나오는건데, 분할정복을 이용한 병합정렬을 이용하면 다 분할해서 한번의 정렬을 이용해서 완전정렬이 되기 때문에 훨씬 빠르다
O(nlogn) 이므로 대략적으로 50만*(5+log5) 즉, 250만번 정도의 연산을 해야한다.
'''
import sys

n = int(sys.stdin.readline().strip())

num_list = list(map(int,sys.stdin.readline().split()))

result = 0

##병합정렬을 위해 리스트를 절반으로 나누고 합친값을 리턴함.
def merge_split(data_list:list)->list:

    ##리스트가 비어있거나 값이 1개면 나눌 필요가 없음
    if len(data_list) <= 1:
        return data_list
    
    mid = len(data_list)//2
    left_list = merge_split(data_list[:mid])
    right_list = merge_split(data_list[mid:])

    return merge(left_list,right_list)

## 절반으로 나눈 리스트를 정렬하면서 합치는 함수
def merge(left_list:list,right_list:list)->list:

    global result

    ##병합된 결괴를 저장해서 반환할 리스트
    merge_result_list = list()
    ##왼쪽과 오른쪽 기준점 - 어디까지 정렬했는지 체크하는 값
    left_point,right_point = 0,0

    temp_result_count = 0

    ## 1번 케이스,왼쪽 오른쪽 값이 둘다 있을때
    while len(left_list) > left_point and len(right_list) > right_point:
        ## 왼쪽이 더 크면 오른쪽값을 먼저 리스트에 넣고, 스왑 횟수 증가
        if left_list[left_point] > right_list[right_point]:
            merge_result_list.append(right_list[right_point])
            right_point+=1
            temp_result_count += 1
        else:
            merge_result_list.append(left_list[left_point])
            left_point+=1
            result += temp_result_count
    
    ##2번 케이스, 오른쪽 데이터가 없을 경우
    while len(left_list) > left_point:
        merge_result_list.append(left_list[left_point])
        left_point += 1
        result += temp_result_count

    ##3번 케이스, 왼쪽 데이터가 없을 경우
    while len(right_list) > right_point:
        merge_result_list.append(right_list[right_point])
        right_point+= 1

    
    return merge_result_list

print(merge_split(num_list))

print(result)