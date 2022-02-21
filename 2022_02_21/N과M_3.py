#백준 N과 M(3) 15651 - 실버3
'''재귀를 이용함'''
#1. 리스트를 인자로 받고, 숫자를 하나 append한후 다시 자기 자신을 호출한다.
#2. 만약 최대길이(m)에 도달하게 되면 해당리스트를 출력하고, 그게 아니면 반복문을 돌면서 값을 추가한다.
#3. 값추가 - 자기 자신 호출 후에는 넣었던 숫자를 빼준다. => 1,--- 첫숫자를 1로 고정하고 반복후에, 다시 이 숫자를 2로 바꾸기 위해서 1로 고정했을때 모든 탐색이 끝나면 pop을 해서 다음 숫자를 넣도록 하는것이다.
'''
import sys


n,m = map(int,sys.stdin.readline().split())

def num(result:list,list_length:int)-> None:

    if list_length == m:
        print(' '.join(list(map(str,result))))
        return 

    for i in range(1,n+1):
        result.append(i)
        num(result,list_length+1)
        result.pop()


num(list(),0)
'''

'''중복순열'''
# 사실 이방법은 나올수 있는 모든 조합을 사용하는 것으로  재귀를 쓰는 것보다 단순 반복문이나, 중복순열 라이브러리를 쓰면 빠르다.
import sys
from itertools import product


n,m = map(int,sys.stdin.readline().split())

num_list = [i for i in range(1,n+1)]

for i in product(num_list,repeat=m):
    print(' '.join(list(map(str,i))))

