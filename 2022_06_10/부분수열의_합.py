#백준 1182번 (백트래킹, 실버2)
import sys

n,s = map(int,sys.stdin.readline().split())

num_list = list(map(int,sys.stdin.readline().split()))


result = 0


def back_tracking(index:int,sum_list:list):
    
    global result
    global num_list


    if index >= n:
        return

    sum_list.append(num_list[index])

    if len(sum_list) != 0 and sum(sum_list) == s:
        result+=1

    
    ## 현재위치의 값을 선택했을떄
    back_tracking(index+1,sum_list)

    ## 현재위치의 값을 선택하지 않았을때,
    sum_list.pop()
    back_tracking(index+1,sum_list)
    



back_tracking(0,list())
print(result)