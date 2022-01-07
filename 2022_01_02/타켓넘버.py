#프로그래머스 level2 타겟넘버
from collections import deque


def solution(numbers, target):
    answer = 0

    queue = deque([(0,numbers[0]*(-1)),(0,numbers[0])])

    while queue: 
        temp_index, temp_value = queue.popleft()

        if temp_index == len(numbers) - 1:
            if temp_value == target:
                answer += 1
            else:
                pass
        
        else:
            temp_index += 1
            queue.append((temp_index,temp_value + numbers[temp_index]*(-1)))
            queue.append((temp_index,temp_value + numbers[temp_index]))

    return answer


#테스트 케이스
if __name__ == "__main__":
    numbers = [1,1,1,1,1]
    target = 3

    assert solution(numbers,target) == 5