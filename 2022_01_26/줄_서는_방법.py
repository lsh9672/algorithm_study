#프로그래머스 level3 - 줄 서는 방법
from itertools import permutations as pm


#정확성 테스트중 2개가 시간초과가 난 풀이 - 순열을 이용해서 모든경우를 구하니, 시간초과가 났다.
def solution(n, k):
    answer = []
    
    human_list = [i for i in range(1,n+1)]
    
    temp = list(pm(human_list,n))[k-1]

    for i in temp:
        answer.append(int(i))

    
    return answer


"""속도를 올리기 위한 풀이"""
#팩토리얼 계산 함수
def fac(num:int) -> int:

    total = 1
    for i in range(1,num+1):
        total *= i

    return total


def solution2(n:int,k:int) -> list:
    answer = []

    #사람 나열
    human_list = [i for i in range(1,n+1)]
    
    while n != 0:

        #몇개씩 있는지 - 앞에 숫자를 고정했을때 몇개씩 경우가 나오는지 계산
        temp = fac(n)//n

        #앞에 고정할 사람의 순번
        passed_people = k // temp


        k = k % temp

        #나눈 나머지가 0이 아니면 k//temp만큼 지나치고 (k//temp)+1번째 사람이라는뜻
        if k != 0:
            answer.append(human_list.pop(passed_people))
        else:
            answer.append(human_list.pop(passed_people-1))
        
        n -= 1

    return answer

"""재귀로 풀어본 풀이 => 효율성에서 시간초과가 난다"""
def calculate(answer:list,human_list:list,k:int,n:int) -> list:

    if n == 0:
        return answer
    
    else:

        temp = fac(n)//n

        passed_people = k // temp


        if (k % temp) != 0:
            answer.append(human_list.pop(passed_people))
        else:
            answer.append(human_list.pop(passed_people-1))
        
        
        return calculate(answer,human_list,k%temp,n-1)


def solution3(n,k):
    answer = []
    #사람 나열
    human_list = [i for i in range(1,n+1)]

    return calculate(answer,human_list,k,n)

if __name__ == "__main__":

    n = 3
    k = 5
    print(solution3(n,k))
    assert solution3(n,k) == [3,1,2]