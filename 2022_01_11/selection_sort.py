#선택 정렬
import random


class SelectionSort:

    def __init__(self):
        self.sorted_list = None

    def swap(self,swap_list:list,index:int,min_index:int)->list:
        swap_list[index], swap_list[min_index] = swap_list[min_index], swap_list[index]

        return swap_list

    def sort(self,non_sorted_list:list) -> list:

        list_length = len(non_sorted_list)

        for i in range(list_length):
            min_index = i
            for j in range(i,list_length):
                if non_sorted_list[min_index] > non_sorted_list[j]:
                    min_index = j
            
            non_sorted_list = self.swap(non_sorted_list,i,min_index)

        self.sorted_list = non_sorted_list
        return self.sorted_list

if __name__ == "__main__":
#삽입 정렬 객체 생성
    selection_sort = SelectionSort()

    #0부터 99중에 50개를 무작위로 뽑음
    random_list = random.sample(range(100),50)
    print(random_list)

    #정렬
    sorted_list = selection_sort.sort(random_list)
    print(sorted_list)