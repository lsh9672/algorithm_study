#백준 17255번 (골드4, 자료구조)

'''
풀이가 생각이 안나서 구글링함
백트래킹 문제이다.
'''
import sys

sys.setrecursionlimit = 10**6


input_string = sys.stdin.readline().strip()


def dfs(left_loc,right_loc,save_path:str):
    global result

    if len(save_path) == target_length:
        result.add(save_path)

    if left_loc > 0:
        dfs(left_loc-1,right_loc, save_path+input_string[left_loc-1:right_loc+1])

    if right_loc < len(input_string):
        dfs(left_loc,right_loc+1, save_path + input_string[left_loc:right_loc+2])

    

result = set()

target_length = len(input_string) * (len(input_string)+1) // 2

for i in range(len(input_string)):
    dfs(i,i,input_string[i])

print(len(result))

