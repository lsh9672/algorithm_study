#백준 9663번 (N-queen)
'''
import sys

시간초과난 풀이
n = int(sys.stdin.readline())


def dfs(queen_list:list,row:int)->int:

    count = 0

    if n == row:
        return 1

    for i in range(n):
        queen_list.append(i)

        if check(queen_list,row):
            count += dfs(queen_list,row+1)
        
        queen_list.pop()
    

    return count

def check(queen_list:list,row)-> bool:

    
    for i in range(row):
        if queen_list[i] == queen_list[row] or row-i == abs(queen_list[row]-queen_list[i]):

            return False

    return True

#한 행에는 1개의 퀸밖에 놓일수 없기 때문에 1차원 배열 이용
print(dfs(list(),0))
'''
import sys


n = int(sys.stdin.readline())

count = 0
queen_list = [0] * n
visited = [False] *n

def dfs(row):

    global count

    if n == row:
        count+=1

    else:
        for i in range(n):
            if visited[i]:
                continue
            queen_list[row] = i

            if check(row):
                visited[i] = True
                dfs(row+1)
                visited[i] = False


def check(row):

    for i in range(row):
        if row-i == abs(queen_list[i] - queen_list[row]):

            return False

    return True

dfs(0)
print(count)