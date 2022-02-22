#백준 15655번 - n과m (6)
import sys

n,m = map(int,sys.stdin.readline().split())

cal_list = list(map(int,sys.stdin.readline().split()))

cal_list.sort()

def num(result):

    if len(result) == m:
        print(" ".join(list(map(str,result))))
        return

    for i in cal_list:
        if i not in result:
            if len(result) == 0:
                result.append(i)
            elif result[-1] < i:
                result.append(i)

            else:
                continue
        else:
            continue
        num(result)
        result.pop()

num(list())
