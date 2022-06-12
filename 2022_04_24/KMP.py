#KMP 알고리즘 연습

## 문자열 탐색에서 점프하는 과정을 구하기 위해 , 실패함수를 정의
## 접두사==접미사 일떄 최대 길이를 저장하는 함수
from sys import prefix

##실패한 테이블 찾는 함수
def makeTable(pattern):

    table = [0 for _ in range(len(pattern))]

    j = 0

    for i in range(1,len(pattern)):
        while j>0 and pattern[i] != pattern[j]:
            j = table[j-1]
        
        if pattern[i] == pattern[j]:
            j+=1
            table[i] = j
    return table

print(makeTable("ABAABAB"))
