#버블 소트
import random

class BubbleSort:

    def __init__(self):
        self.sorted_list = None

    def swap(self,swap_list:list,j:int)->list:
        swap_list[j], swap_list[j+1] = swap_list[j+1], swap_list[j]

        return swap_list

    def sort(self,non_sorted_list:list) -> list:
        list_length = len(non_sorted_list)

        for i in range(list_length):
            #스왑하는 것이 없으면 더이상 정렬할것이 없기때문에 종료
            swap_check = False
            for j in range(list_length - 1 - i):
                if non_sorted_list[j] > non_sorted_list[j+1]:
                    swap_check = True
                    non_sorted_list = self.swap(non_sorted_list,j)
            #swap_check 변수가 False면 스왑이 일어나지 않음 , 즉 정렬완료        
            if swap_check == False:
                self.sorted_list = non_sorted_list
                return self.sorted_list 

        self.sorted_list = non_sorted_list
        return self.sorted_list

        
if __name__ == "__main__":
    #버블 소트 객체 생성
    bubble_sort = BubbleSort()

    #0부터 99중에 50개를 무작위로 뽑음
    random_list = random.sample(range(100),50)
    print(random_list)

    #정렬
    sorted_list = bubble_sort.sort(random_list)
    print(sorted_list)

    for i in range(10,-1,-1):
        print(i)
    
            
        

