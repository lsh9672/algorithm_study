# 백준 16916번(KMP를 이용한 풀이)
import sys

input_string = sys.stdin.readline().strip()

pattern = sys.stdin.readline().strip()

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

def kmp(input_string:str, pattern:str):
    
    table = makeTable(pattern)

    j = 0

    for i in range(len(input_string)):
        while j > 0 and input_string[i] != pattern[j]:
            j = table[j - 1]

        if input_string[i] == pattern[j]:
            if j == len(pattern) - 1:
                return 1

            else:
                j+=1

    return 0

print(kmp(input_string,pattern))