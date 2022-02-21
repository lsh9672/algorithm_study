#백준16918 봄버맨 실버1

'''아이디어'''
#1. 격자판 상황을 그래프의 노드라고 생각했고, 자식노드는 1초뒤의 격차판 상황으로 생각했다.
#2. 우선 현재 몇초가 흐른 폭탄인지 확인하지 위해서 빈칸은 -1, 폭탄은 0으로 둔다.
#3. 매초, 즉 자식노드를 찾을때 모든 값들을 +1한다
#4. 돌면서 3인 값의 상하좌우를 터트린다.

import sys

r,c,n = map(int,sys.stdin.readline().split())

#빈칸은 -1로 표기, 초기값을 -1로 표기하고 반복문을 돌면서 입력값에서 폭탄을 찾아서 1로 바꿔준다(원래 0인데, 문제에서 처음에는 1초간 아무것도 안한다해서 1로 만듦)
graph = [[-1 for _ in range(c)] for _ in range(r)]

#몇초가 흘렀는지 세는 변수(시작1초간 아무것도 안하기 때문에 1초부터 시작)
count = 1


#격자판 채우기
for i in range(r):
    #한줄을 받음
    temp = sys.stdin.readline()
    for j in range(c):
        if temp[j] == "O":
            graph[i][j] = 1


#폭탄을 터트릴 상하좌우 좌표정의
dx = [0,0,-1,1]
dy = [-1,1,0,0]

while count<n:

    #1씩 증가시키면서 3인 값의 좌표를 저장해둠
    temp_list = list()
    
    #우선 모든 값을 1씩 증가시킴
    for i in range(r):
        for j in range(c):
            graph[i][j]+=1
            if graph[i][j] == 3:
                temp_list.append([i,j])
 
    #이중에서 3인 값을 찾아서 
    for a,b in temp_list:
        #혹시 이미 터졌을수도 있으니 3인지 한번더 확인하고 터트림
        
        graph[a][b] = -1
        #상하좌우 전부 -1로 만듦
        for k in range(4):
            next_a,next_b = a+dx[k],b+dy[k]
            if next_a >= 0 and next_a < r and next_b >=0 and next_b<c:
                graph[next_a][next_b] = -1
    
    count+=1

# 결과 출력용 리스트
result = list()

#최종 그래프를 주어진 문제에 맞게 O, . 으로 바꿈
#바꾸면서 행은 문자열로 만들어서 결과 리스트에 넣음
for i in range(r):
    temp = ""
    for j in range(c):
        #-1이면 빈칸
        if graph[i][j] == -1:
            temp += "."
        else:
            temp += "O"
    result.append(temp)

for i in result:
    print(i)


