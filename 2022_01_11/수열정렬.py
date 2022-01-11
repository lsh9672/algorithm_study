'''
정리하면 자신이 몇번째로 작은 값인지를 나타내는 것
2 3 1 이면 => 2는 1번째로 작고 3은 2번째로 작고 1은 0번째로 작다
따라서 1 2 0 이 되는 것이다.
'''

import sys


def solution(num_list : list)->list:
    temp = sorted(num_list)
    
    return_list = list()

    for a in num_list:
        return_list.append(str(temp.index(a)))
        #같은 값이 있을수도 있기 때문에 중복을 피하기 위해 탐색한 값은 -1로 변경
        temp[temp.index(a)] = -1
    
    return return_list

#수열의 크기
n = int(sys.stdin.readline())

#수열
temp_list = list(map(int,sys.stdin.readline().split()))

sys.stdout.write(" ".join(solution(temp_list)))