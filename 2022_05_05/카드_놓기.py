#백준 5568번 (자료구조 연습)
import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())

num_list = list()
for _ in range(n):
    num_list.append(sys.stdin.readline().strip())



def recursive(count:int,temp_list:list):
    global result

    if count == k:
        result.add("".join(temp_list))
        return

    for i in range(n):
        if visited[i] == 1:
            continue

        temp_list.append(num_list[i])
        visited[i] = 1
        recursive(count+1,temp_list)
        temp_list.pop()
        visited[i] = 0

visited = [0]*n
result = set()

recursive(0,list())


print(len(result))
