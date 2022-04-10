# 백준 2800번 (자료구조,괄호 제거)

'''아이디어'''
#좌표 쌍 위치 인덱스를 찾는다.
#찾은 좌표를 조합을 이용해서 삭제할 괄호를 구한다.
#특정 좌표를 지우기 위해서는 list로 변경이 필요하다
#list로 문자열을 변경한후에, 괄호를 빈값으로 만들고(삭제하면 인덱스에 문제가 생김), join을 이용해서 문자열로 만든다
#이렇게 만들어진 수식을 중복이 있을수도 있기 떄문에, set에 넣어서 중복을 제거해준다.
#출력시에 사전순으로 해야되기 떄문에 리스트로 변경후 정렬한다.
#제거할 괄호쌍은 뭘 먼저 제거하든 상관없기 때문에, 조합을 이용한다.

import sys
from itertools import combinations


formula = sys.stdin.readline().strip()

#인덱스를 저장해둠
bracket_stack = []

#스택을 이용해서 괄호쌍의 위치를 구함.
bracket_location = list()

temp = list()
for i in range(len(formula)):
    if formula[i] == "(":
        bracket_stack.append(i)

    elif formula[i] == ")":
        temp.append(bracket_stack.pop())
        temp.append(i)

        bracket_location.append(temp)

        temp = list()

result = set()

for i in range(1,len(bracket_location)+1):
    bracket_combination = combinations(bracket_location,i)

    for temp in bracket_combination:
        formula_list = list(formula)

        for select_bracket in temp:
            start,end = select_bracket

            formula_list[start] = ""
            formula_list[end] = ""

        #괄호를 다지웠으면 합치고 집합에 넣기
        result.add("".join(formula_list))

result =sorted(list(result))

for i in result:
    print(i)
