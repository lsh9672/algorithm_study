#삽입정렬
import random

class InsertionSort:

    def __init__(self):
        self.sorted_list = None

    def swap(self,swap_list:list,j:int)->list:
        swap_list[j], swap_list[j-1] = swap_list[j-1], swap_list[j]

        return swap_list

    def sort(self, non_sorted_list: list)-> list:
        list_length = len(non_sorted_list)
        for i in range(1,list_length):
            for j in range(i,0,-1):
                if non_sorted_list[j] < non_sorted_list[j-1]:
                    non_sorted_list = self.swap(non_sorted_list,j)
                else:
                    break
        self.sorted_list = non_sorted_list
        return self.sorted_list
                

if __name__ == "__main__":
    #삽입 정렬 객체 생성
    insertion_sort = InsertionSort()

    #0부터 99중에 50개를 무작위로 뽑음
    random_list = random.sample(range(100),50)
    print(random_list)

    #정렬
    sorted_list = insertion_sort.sort(random_list)
    print(sorted_list)