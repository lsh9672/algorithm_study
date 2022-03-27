#백준 9342번 (문자열, 실버4) - 정규 표현식 사용
import sys
import re

#입력
t = int(sys.stdin.readline())

#검증 할 정규 표현식
regex = re.compile('^[A-F]{0,1}A+F+C+[A-F]{0,1}$')

result = list()

for _ in range(t):
    test_case = sys.stdin.readline().strip()

    result.append(regex.match(test_case))


for i in result:
    if i != None:
        print("Infected!")

    else:
        print("Good")

