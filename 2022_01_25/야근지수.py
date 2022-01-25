#프로그래머스 level3 야근지수


'''효율성에서 통과를 못함 - max함수는 굉장히 느리다'''
def solution(n, works):
    answer = 0

    total_works = sum(works)

    #남은 일의 총량이 퇴근시간보다 작으면 0
    if total_works <= n:
        return 0

    #남은 시간만큼 works 중에 최대값을 찾아서 -1 씩함(남은 시간을 다 쓸때까지)
    for _ in range(n):
        #최대값이 있는 인덱스를 찾아서 빼줌
        works[works.index(max(works))] -= 1

    for i in works:
        answer += i*i


    return answer



'''속도 개선을 위한 코드
매연산마다 최대값을 찾아야됨 -> maxheap을 이용 -> 파이썬의 heapq는 min heap만 제공-> 각 숫자에 -를 붙여주면 max처럼 동작하게 할수있음
'''
import heapq


def solution2(n, works):
    answer = 0

    #남은 일의 총량이 퇴근시간보다 작으면 0
    if sum(works) <= n:
        return 0

    #힙 자료구조
    queue = list()

    #works를 heap에 넣어줌 -> max으로 동작시키기 위해서 -1을 곱해서 넣음
    for i in works:
        heapq.heappush(queue,i*(-1))

    #works를 균등하게 나누기 위해서 반복문을 돌면서 가장 큰값 -1을함
    for _ in range(n):
        #힙에서 뻄
        temp = heapq.heappop(queue)

        #뺀값에 +1을해서(원래-1인데 최대힙으로 만들기 위해서 -1을 곱해줬으니 +1을 해줌)
        #+1을 하고 다시 힙에 넣음
        heapq.heappush(queue,temp+1)
    
    #최종적으로 나열된 값들을 야근지수공식에 맞게 계산함
    for i in queue:
        answer += i*i
        
    return answer

if __name__ == "__main__":
    n = 4
    works = [4,3,3]
    assert solution2(n,works) == 12

    n = 1
    works = [2,1,2]
    assert solution2(n,works) == 6

    n = 3
    works = [1,1]
    assert solution2(n,works) == 0
