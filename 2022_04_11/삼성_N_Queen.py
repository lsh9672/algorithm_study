#SWEA - d3
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_04_11/input.txt","r")

T = int(input())

def check(queen_location:list,row:int)-> bool:
    for i in range(row):

        if queen_location[row] == queen_location[i] or abs(queen_location[row]-queen_location[i]) == row-i:
            return False
    return True

def dfs(queen_location:list,row:int)-> int:
    length = len(queen_location);

    count = 0

    if length == row:
        return 1

    for i in range(length):

        queen_location[row] = i

        if check(queen_location,row):
            count += dfs(queen_location,row+1)

    return count

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())

    queen_location = [0]*n

    result = dfs(queen_location, 0)

    print(f"#{test_case} {result}")
