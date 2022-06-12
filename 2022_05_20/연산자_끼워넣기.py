#백준 14888번 (백트래킹, 실버1)
import sys

n = int(sys.stdin.readline().strip())

num_list = list(map(int,sys.stdin.readline().split()))


## +,-,*,/ 순서대로 각각의 개수를 나타냄
operator_list = list(map(int,sys.stdin.readline().split()))

max_value = -1e9
min_value = 1e9

## 최대 개수(n)까지 반복했는지 확인할 count변수와, 연산한 결과를 넘겨줄 operation_value를 인자로 받는다.
def dfs(count:int,operation_value:int)-> None:
    ## 매 함수 호출마다 최대,최소값을 업데이트하고, 연산자 수를 업데이트 하기위해서 전역변수로 설정함
    global operation_list,max_value,min_value

    ## 최대개수에 도달하면 최대,최소값 구하고 리턴
    if count == n:
        max_value = max(operation_value,max_value)
        min_value = min(operation_value,min_value)
        return

    ## 도달안헀으면 각 연산자중에 남아있는 연산 실행
    else:
        ## 덧셈
        if operator_list[0] > 0:
            operator_list[0] -= 1
            dfs(count+1,operation_value + num_list[count])
            operator_list[0] += 1

        ## 뺄셈
        if operator_list[1] > 0:
            operator_list[1] -= 1
            dfs(count+1,operation_value - num_list[count])
            operator_list[1] += 1


        ## 곱셈
        if operator_list[2] > 0:
            operator_list[2] -= 1
            dfs(count+1,operation_value * num_list[count])
            operator_list[2] += 1

        ## 나눗셈
        if operator_list[3] > 0:
            operator_list[3] -= 1
            ## 문제에 나와있는대로 나누기를 하고 몫만 취하려면 //가 아닌 /후에 정수로 형변환해서 소수점을 날리는 연산이 필요하다.
            dfs(count+1,int(operation_value / num_list[count]))
            operator_list[3] += 1
    return

dfs(1,num_list[0])

print(max_value)
print(min_value)