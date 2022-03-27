#벡준 11656번 (문자열 연습, 실버4)
import sys

#입력
s = sys.stdin.readline().strip()

#결과 리스트를 선언한다.
result = list()

#입력된 문자의 길이만큼, 반복하면서 앞에 단어부터 하나씩 자르고 결과 리스트에 넣는다.
for i in range(len(s)):

    result.append(s[i:])

#결과 리스트를 정렬해서 사전순으로 만든다.

result.sort()

#순서대로 출력한다.

for i in result:
    print(i)