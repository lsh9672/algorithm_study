#백준15656번 - N과M_7(실버3, 백트래킹)
import sys


n,m = map(int,sys.stdin.readline().split())

#입력받은 숫자를 리스트로 만듦
num_list = list(map(int,sys.stdin.readline().split()))

#사전순으로 출력하기 위해 정렬
num_list.sort()

#결과를 담을 리스트
result = [0 for i in range(m)]

#결과가 어디까지 채워졌는지 확인하는 값
count = 0


#재귀로 반복하면서 결과를 출력하는 함수
def dfs(result:list,count:int)->None:

    if count == m:
        #join으로 찍을라면 str이어야됨
        print(" ".join(list(map(str,result))))
        return
    
    for i in num_list:
        result[count]=i
        dfs(result,count+1)

            
dfs(result,count)