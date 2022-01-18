#이진탐색 구현
import random 

#재귀 이용
def binary_search(search_data:int,search_list:list,low=None,high=None) -> int:
    low,high = low or 0 , high or len(search_list)-1
    
    if low > high:
        return -1

    mid = (low+high) // 2
    if search_list[mid] > search_data:
        return binary_search(search_data,search_list,low,mid-1)

    if search_list[mid] == search_data:
        return mid
    if search_list[mid] < search_data:
        return binary_search(search_data,search_list,mid+1,high)

#재귀x
def binary_search2(search_data:int,search_list:list)-> int:
    low,high = 0,len(search_list)-1

    while low <= high:
        mid = (low+high) //2

        if search_list[mid] > search_data:
            high = mid -1

        if search_list[mid] == search_data:
            return mid
        
        if search_list[mid] < search_data:
            low = mid+1

    return -1


if __name__ == "__main__":
    temp_list = random.sample(range(100),100)
    temp_list.sort()

    temp_index1 = binary_search(search_list = temp_list,search_data = 48)
    temp_index2 = binary_search2(search_list = temp_list,search_data = 48)
    
    print(f"재귀 이용, index : {temp_index1}, value : {temp_list[temp_index1]}")
    print(f"반복 이용, index : {temp_index2}, value : {temp_list[temp_index2]}")

    assert binary_search(search_list = temp_list,search_data = 48) == binary_search2(search_list = temp_list,search_data = 48)