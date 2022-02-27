#백준 15652번 - n과m (4)
import sys


n,m = map(int,sys.stdin.readline().split())


def num(result:list)->None:

    if len(result) == m:
        print(" ".join(map(str,result)))
        return

    for i in range(1,n+1):
        if len(result) == 0:
            result.append(i)
        elif result[-1] <= i:
            result.append(i)

        else:
            continue

        num(result)
        result.pop()
        

num(list())