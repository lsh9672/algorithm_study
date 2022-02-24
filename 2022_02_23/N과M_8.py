#백준 15657번 N과M(7) 실버3 (백트래킹)
import sys


n,m = map(int,sys.stdin.readline().split())

num_list = list(map(int,sys.stdin.readline().split()))

num_list.sort()


def dfs(result:list,count:int) -> None:

    if count == m:
        print(" ".join(list(map(str,result))))
        return 

    
    for i in num_list:
        if count == 0:
            result[count] = i

        elif result[count-1] <= i:
            result[count] = i

        else:
            continue
        
        dfs(result,count+1)

result = [0 for i in range(m)]

dfs(result,0)