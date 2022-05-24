#백준 15953

import sys


n = int(sys.stdin.readline().strip())

first_list = [0,1,3,6,10,15,21]
first_dict = {1:5000000,2:3000000,3:2000000,4:500000,5:300000,6:100000}
second_list = [0,1,3,7,15,31]
second_dict = {1:5120000,2:2560000,3:1280000,4:640000,5:320000}

for _ in range(n):
    total = 0
    a,b = map(int,sys.stdin.readline().split())

    if a <= 21:
        for i in range(1,len(first_list)-1):
            if first_list[i] >= a:
                total += first_dict[i]
                break


    if b <= 31:
        for i in range(1,len(second_list)-1):
            if second_list[i] >= a:
                total += second_dict[i]
                break
    
    print(total)
