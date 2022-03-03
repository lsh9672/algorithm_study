#백준 20291 - 파일정리(실버3)
import sys


test_case = int(sys.stdin.readline())

file_evt = dict()

for _ in range(test_case):

    a,b = sys.stdin.readline().strip().split(".")

    if b not in file_evt:
        file_evt[b] = 1
    
    else:
        file_evt[b]+=1

result = list(file_evt.items())

result.sort()

for a,b in result:
    print(a,b)