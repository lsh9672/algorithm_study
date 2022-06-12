#백준 - 4889번(실버1, 문자열 연습)

'''접근 아이디어
이전에 풀었던 괄호 문제들에서 한걸음 더 나아가면된다.
닫는 괄호가 아니면 스택에 넣고, 닫는괄호이면, 스택에서 맨위의 값을 빼는식으로 진행한다.
입력으로 주어진 모든 괄호를 이 과정을 거치고 나면, 안정적이지 않은 괄호들이 남는다.
이 괄호들을 하나씩 꺼내서 괄호의 방향을 바꿨을떄 안정적인 괄호가 되는지 확인해서 그 수를 센다.
'''



import sys
#출력을 위해 순번 저장
num_count = 0

while True:
    
    num_count += 1

    change_count = 0

    brackets = sys.stdin.readline().strip()

    if "-" in brackets:
        break

    bracket_check_stack = list()

    for bracket in brackets:
        if bracket == "{":
            bracket_check_stack.append(bracket)
        
        # } 이면
        else:
            
            #스택이 비어잇다면
            if len(bracket_check_stack) == 0:
                bracket_check_stack.append(bracket)

            #비어있지 않다면
            else:
                #최상단 값이 여는 괄호인지 확인
                if bracket_check_stack[-1] == "{":
                    #여는 괄호이면 출력
                    bracket_check_stack.pop()

                else:
                    #닫는 괄호라면, 스택에 넣음
                    bracket_check_stack.append(bracket)

    #반복이 끝났을떄, 스택이 비었으면, 불안정한문자가 없는것
    if len(bracket_check_stack) == 0:
        print(f"{num_count}. {change_count}")

    else:

        #안정된 문자열이 되는지 확인
        check_bracket = ""

        #남은 스택안의 불안정한 괄호를 하나씩 꺼내서 안정된 괄호로 만듦
        while bracket_check_stack:

            temp_bracket = bracket_check_stack.pop()

            #꺼냈을떄, 이전에 꺼내놓은것이 있는지 없는지로 나뉨
            if check_bracket == "":
                #꺼냈는데 여는 괄호면, 무조건 돌려야
                if temp_bracket == "{":
                    change_count+=1
                    check_bracket = "}" + check_bracket
                
                #닫는 괄호
                else:
                    check_bracket = temp_bracket 
            
            #꺼냈는데 이전에 꺼내둔 것이 있다면,
            else:
                #여는괄호
                if temp_bracket == "{":
                    check_bracket = temp_bracket + check_bracket
                
                #닫는 괄호
                else:
                    change_count+=1
                    check_bracket = "{" + check_bracket

            if check_bracket == "{}":
                check_bracket = ""

        print(f"{num_count}. {change_count}")