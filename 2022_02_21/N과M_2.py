#백준 15650번 - 실버3 N과M_2

import sys


n,m = map(int, sys.stdin.readline().split())

result = list()

def num(result):

    if len(result) == m:
        print(' '.join(list(map(str,result))))
        return
    

    for i in range(1,n+1):
        if i not in result:
            if len(result) >0 and result[-1] > i:
                continue

            result.append(i)
            num(result)
            result.pop()   
            

num(result)