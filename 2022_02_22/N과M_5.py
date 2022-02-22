#백준 15652번 - n과m (5)
import sys


n,m = map(int,sys.stdin.readline().split())


cal_list = list(map(int,sys.stdin.readline().split()))

cal_list.sort()


def num(result:list)->None:

    if len(result) == m:
        print(" ".join(list(map(str,result))))
        return
    
    for i in cal_list:
        if i not in result:
            result.append(i)
            num(result)
            result.pop()

num(list())