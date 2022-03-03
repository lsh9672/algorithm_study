#백준 16935번 (배열돌리기, 구현연습, 실버1)
import sys


#세로, 가로, 명령어 수 
n,m,r = map(int, sys.stdin.readline().split())

array = list()

#배열 입력받기
for _ in range(n):

    array.append(list(map(int,sys.stdin.readline().split())))

#명령어 입력받기

command = list(sys.stdin.readline().split())

#상하 반전
def cal_1():
    temp_array = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        temp_array[i] = array[n-i-1]
    
    return temp_array

#좌우 반전
def cal_2():
    temp_array = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(m):
        for j in range(n):
            temp_array[j][m-1-i] = array[j][i]
    return temp_array

#오른쪽으로 90도 회전
def cal_3(n,m):

    temp_array = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp_array[i][j] = array[n-1-j][i]

    return temp_array

#왼쪽으로 90도 회전
def cal_4(n,m):

    temp_array = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            temp_array[i][j] = array[j][m-1-i]

    return temp_array


#1번 그룹->2번그룹, 2번그룹->3번그룹, 3번그룹-> 4번그룹, 4번 그룹-> 1번그룹
def cal_5():
    temp_array = [[0 for _ in range(m)] for _ in range(n)]
    #n/2,m/2
    #1번 그룹->2번그룹
    for i in range(n//2):
        for j in range(m//2):
            temp_array[i][j+(m//2)] = array[i][j]

    #2번그룹->3번그룹
    for i in range(n//2):
        for j in range(m//2,m):
            temp_array[i+(n//2)][j] = array[i][j]

    #3번그룹-> 4번그룹
    for i in range(n//2,n):
        for j in range(m//2,m):
            temp_array[i][j-(m//2)] = array[i][j]

    #4번 그룹-> 1번그룹
    for i in range(n//2,n):
        for j in range(m//2):
            temp_array[i-(n//2)][j] = array[i][j]

    return temp_array


#1번 그룹->4번그룹, 4번그룹->3번그룹, 3번그룹-> 2번그룹, 2번 그룹-> 1번그룹
def cal_6():
    temp_array = [[0 for _ in range(m)] for _ in range(n)]
    #1번 그룹->4번그룹
    for i in range(n//2):
        for j in range(m//2):
            temp_array[i+(n//2)][j] = array[i][j]

    #4번그룹->3번그룹
    for i in range(n//2,n):
        for j in range(m//2):
            temp_array[i][j+(m//2)] = array[i][j]

    #3번그룹-> 2번그룹
    for i in range(n//2,n):
        for j in range(m//2,m):
            temp_array[i-(n//2)][j] = array[i][j]


    #2번 그룹-> 1번그룹
    for i in range(n//2):
        for j in range(m//2,m):
            temp_array[i][j-(m//2)] = array[i][j]

    return temp_array


for i in command:
    if i == "1": array = cal_1()
    elif i == "2": array = cal_2()
    elif i == "3": 
        array = cal_3(n,m)
        n,m = m,n
    elif i == "4": 
        array = cal_4(n,m)
        n,m=m,n
    elif i == "5": array = cal_5()
    elif i == "6": array = cal_6()

for i in range(len(array)):
    for j in range(len(array[0])):
        print(array[i][j],end=" ")
    
    print("")
