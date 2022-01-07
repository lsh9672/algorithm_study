#프로그래머스 level2 프린터
from collections import deque


def solution(priorities, location):
    answer = 0
    
    #출력해야되는 것
    output = (location,priorities[location])

    temp_list = []
    for a,b in enumerate(priorities):
        temp_list.append((a,b))

    queue = deque(temp_list)

    
    #탐색
    while True:
    
        print_value = queue.popleft()
        
        for i in queue:
            if print_value[1] < i[1]:
                queue.append(print_value)
                break
        #끝까지 탐색했는데 자신보다 우선순위가 큰 것이 없다면 
        else:
            answer+=1
            if print_value == output:
                break

    return answer


#테스트 케이스
if __name__ == "__main__":
    priorities = [2,1,3,2]
    location = 2
    assert solution(priorities,location) == 1

    priorities = [1,1,9,1,1,1]
    location = 0
    assert solution(priorities,location) == 5