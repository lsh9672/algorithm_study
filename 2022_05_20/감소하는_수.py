#백준 1174번(골드5,백트래킹)
import sys

n = int(sys.stdin.readline().strip())

## 몇번째 수인지 체크할 변수
count = set()


def dfs(save_list:list):
    global count

    if len(save_list)>0:
        count.add(int("".join(save_list)))

    for i in range(10):
        if len(save_list) == 0 or int(save_list[-1]) > i:
            save_list.append(str(i))
            dfs(save_list)
            save_list.pop()
try:
    dfs(list())
    count = list(count)
    count.sort()
    
    print(count[n-1])
except:
    print(-1)