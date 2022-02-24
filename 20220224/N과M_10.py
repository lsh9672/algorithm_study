#백준 15664번 N과M(10)
import sys



n,m = map(int,sys.stdin.readline().split())

num_list = list(map(int,sys.stdin.readline().split()))

num_list.sort()



def dfs(result:list,count:int)-> list:

    if count == m:
        temp = " ".join(list(map(str,result)))
        if temp not in check_dict:
            check_dict[temp] = 1
            print(temp)
        return 
        
    for i in range(n):
        if index_check[i] == -1:
            continue
        if count == 0:
            result[count] = num_list[i]
        elif result[count-1] <= num_list[i]:
            result[count] = num_list[i]
        else:
            continue
        index_check[i] = -1 
        dfs(result,count+1)
        index_check[i] = 0

result = [0 for _ in range(m)]

check_dict = dict()

index_check = [0 for _ in range(n)]

dfs(result,0)

