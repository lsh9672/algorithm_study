## SWEA 2063번(중간값 찾기 - D1)

import sys
sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_04_17/input.txt", "r")

n = int(input())

temp_list = list(map(int,input().split()))

temp_list.sort()

print(temp_list[(n-1)//2])
    
