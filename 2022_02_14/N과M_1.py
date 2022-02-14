#백준 15649번 N과M(1), 백트래킹

'''아이디어'''
#1. 백트래킹으로는 생각이 나지 않아 재귀를 이용한 반복을 생각했다
import sys


'''입력'''

n,m = map(int,sys.stdin.readline().split())

result = []

def num()-> None:

    if len(result) == m:
        print(' '.join(map(str,result)))
        return


    for i in range(1,n+1):
        #숫자가 안겹쳐야 되므로 확인함,
        if i not in result:
            result.append(i)
            num()
            result.pop()

num()
