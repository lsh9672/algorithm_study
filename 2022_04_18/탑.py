#백준 2493번 (탑, 골드5)
import sys

n = int(sys.stdin.readline())

tower_list = list(map(int,sys.stdin.readline().split()))

'''아이디어
#무지성으로 반복문 돌려가면서 하나의 탑을 고르고, 그 탑으로부터 왼쪽에 있는 모든 것과 비교하면 대략 O(n^2)가 나온다.
#n의 최대 개수는 500,000이므로 250,000,000,000 => 2천 5백억번이 된다. ㅋㅋㅋ
#따라서 스택을 이용해서 위의 횟수를 좀 줄여보려고 한다.
#주어진 타워의 오른쪽부터 하나씩 스택에 넣을것이다.
#다음에 넣을 값과 스택에 들어있는 최상단 값을 비교해서 다음에 넣을 값이 더 크다면, 그 값이 레이저 신호를 받는 값이 된다.
#그리고 다음 탐색을 위해서 다음에 넣을 값을 넣는다.
'''
stack = []

result_list = [0 for _ in range(n)]

for i in range(len(tower_list)-1,-1,-1):
    #스택이 비어있으면 인덱스와 높이를 리스트로 만들어서 넣음
    if len(stack) == 0:
        stack.append([i,tower_list[i]])
    
    else:
        #최상단 값과 다음에 넣을 값을 비교해서 다음에 넣을 값이 더 크면, 그 값이 수신할 탑임
        #따라서 안에 있는 값들이 보내는 레이저는 다음에 넣을 탑이 수신하기 때문에 스택에서 전부빼서 저장함.
        while tower_list[i] > stack[-1][1]:
            temp = stack.pop()
            result_list[temp[0]] = i+1
            
            if not stack:
                break

        
        stack.append([i,tower_list[i]])

print(*result_list)

