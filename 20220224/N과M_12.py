#백준 15666번 N과M(12) 실버2
import sys


n,m  = map(int,sys.stdin.readline().split())

num_list = list(map(int,sys.stdin.readline().split()))

num_list.sort()

def dfs(result,count):

    if count == m:
        temp = " ".join(list(map(str,result)))
        if temp not in check_dic:
            check_dic[temp] = 1
            print(temp)
        return

    for i in range(n):
        if count == 0:
            result[count] = num_list[i]

        elif result[count-1] <= num_list[i]:
            result[count] = num_list[i]

        else:
            continue

        dfs(result,count+1)



result = [0 for _ in range(m)]

check_dic = dict()

dfs(result,0)


