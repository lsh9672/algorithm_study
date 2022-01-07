#프로그래머스 level 2 가장큰수
from itertools import permutations


def solution(numbers):
    answer = ''
    temp_string = list()
    
    for i in numbers:
        temp_string.append(str(i))
    temp = sorted(temp_string,key = lambda x:x*3,reverse = True)

    answer = int("".join(temp))

    
    
    return str(answer)


if __name__ == "__main__":
    numbers = [6,10,2]

    assert solution(numbers) == "6210"

    numbers = [3,30,34,5,9]
    assert solution(numbers) == "9534330"