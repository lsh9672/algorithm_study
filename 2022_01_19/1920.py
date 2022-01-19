#백준 1920 수찾기 (탐색)

import sys


def binary_search(data:int,search_list:list) -> bool:
    low,high = 0,len(search_list)-1

    while low <=high:
        mid= (low+high)//2

        if search_list[mid] > data:
            high = mid-1
        
        if search_list[mid] == data:
            return True

        if search_list[mid] < data:
            low = mid+1
    
    return False


n1 = int(sys.stdin.readline())

first_list = list(map(int,sys.stdin.readline().split()))

n2 = int(sys.stdin.readline())

second_list = list(map(int,sys.stdin.readline().split()))

#이진탐색 하기전에 정렬

first_list.sort()

for i in second_list:
    if binary_search(i,first_list) == True:
        print(1)
    else:
        print(0)

