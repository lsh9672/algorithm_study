#백준 15665번 N과M(11) - 실버2

import sys


n,m = map(int,sys.stdin.readline().split())

num_list = list(map(int,sys.stdin.readline().split()))

num_list.sort()



def dfs(result:list,count:int)->list:

    if count == m:
        temp = " ".join(list(map(str,result)))
        if temp not in check_dic:
            check_dic[temp] = 1
            print(temp)
        return

    for i in range(n):
        result[count] = num_list[i]
        dfs(result,count+1)

#중복체크
check_dic = dict()

result = [0 for _ in range(m)]

index_check = [0 for _ in range(n)]

dfs(result,0)