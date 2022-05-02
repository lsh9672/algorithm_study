#백준 2776번 (자료구조 연습, 실버4)
import sys


test_case = int(sys.stdin.readline().strip())

for _ in range(test_case):
    n = int(sys.stdin.readline())
    first_list = set(list(map(int,sys.stdin.readline().split())))

    m = int(sys.stdin.readline())
    
    second_list = list(map(int,sys.stdin.readline().split()))
    for i in second_list:
        if i in first_list:
            print(1)
        else:
            print(0)