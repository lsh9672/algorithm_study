#백준 10974번(실버3, 백트래킹)
import sys

n = int(sys.stdin.readline().strip())

def recursive(num_list:list):
    global result
    if len(num_list) == n:
        print(*num_list)
        return 


    for i in range(1,n+1):
        if i not in num_list:
            num_list.append(i)
            recursive(num_list)
            num_list.pop()

recursive(list())
