# 백준알고리즘  1026

'''
두 배열의 각각의 인덱스의 원소끼리 곱하고 나온 모든 결과를 더한 값을 S라고 한다
이 S를 작게 만들어야 한다.
아이디어: 가장 큰값은 가장 작은값과 곱해지게 해서 더하면 가장 작은 값을 얻을 것이라고 생각한다.
따라서 하나의 배열(A)는 오름차순 정렬, 다른 하나의 배열(B)은 내림차순 정렬을 하면 될것이라고 생각한다.
'''
import sys


def solution(array1:list,array2:list)->int:
    #첫번째 배열을 오름차순, 두번째 배열은 reverser=True로 하여서 내림차순으로 정렬한다.
    array1 = sorted(array1)
    array2 = sorted(array2,reverse=True)
    total = 0
    for i in range(len(array1)):
        total += array1[i]*array2[i]

    return total


#입력받기 
#배열의 크기
n = int(sys.stdin.readline())

#배열1 - A
array1 = list(map(int,sys.stdin.readline().split()))

#배열2 - B
array2 = list(map(int,sys.stdin.readline().split()))

#계산하는 함수의 결과 출력
sys.stdout.write(str(solution(array1,array2)))