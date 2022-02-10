#프로그래머스 level3 - N으로 표현하기


def solution(N, number):

    #N == number 이면 표현할수 있는 방법은 1가지임
    if N == number:
        return 1

    #연산 셋을 저장할 집합 - 중복제거를 위해 집합사용
    operator_set = [set() for _ in range(8)]

    #각각 표시할수 있는 N의 수를 나열한다.
    #주어진 조건에 의하면 최대 8번 까지 사용된다 - 8보다 크면 -1을 리턴하게 함.
    #각각의경우 연산자 없이 만들어질수 있는 경우는 N=5로 가정하면 5,55,555....5555555이다
    #이것들을 전부 각 set에 넣어줌(operator_set의 리스트를 하나씩 돌면서 set안에 넣음)
    for a,b in enumerate(operator_set,start=1):
        b.add(int(str(N)*a))

    print(f"fist:{operator_set}")
    #반복문을 돈다
    #i의 의미는 N을 사용한 횟수이다.
    #operator_set[i]는 N을 i번 사용한 횟수이다.
    #operator_set의 경우 인덱스를 0부터 사용하기 때문에 i가 1~7 반복하게 된다.
    #인덱스 8 즉 9개를 사용했을 경우는 문제에서 8개 초과시에는 -1을 리턴하라고 했기 때문에 인덱스를 7까지만 돌리는 것이다.
    #N을 한개만 썼을때인 인덱스 0번쨰는 나올수 있는 경우가 N==number인데, 이경우는 시작부분에서 분기로 처리를 해줬다.
    for i in range(1,8):

        #i = 1이면 0
        #i = 2이면 0,1 이런식으로 반복하도록 함.
        #이렇게 하는 이유는 그 아래 두 반복문에 있음
        #만약 N을 3번 사용했다면 나올수 있는 가지수는 - (1,2),(1,1,1),(2,1)임
        #이를 구현하기 위해서 operator1에는 operator_set에는 j를, operator2에는 i-j-1번째를 가져옴(인덱스를 0부터 사용하기 때문에 이렇게 함.)
        #즉 N이 5이면 1번 사용했을떄와 4번 사용했을때의 식을 각각 사칙연산 , 2,3 / 3,2 / 4,1 이런식으로 진행함.
        print(f"i:{i}")
        for j in range(i):
            print(f"j:{j}, j2: {i-j-1}")
            for operator1 in operator_set[j]:
                for operator2 in operator_set[i-j-1]:
                    operator_set[i].add(operator1 + operator2)
                    operator_set[i].add(operator1 - operator2)
                    operator_set[i].add(operator1 * operator2)
                    if operator2 != 0:
                        operator_set[i].add(operator1 // operator2)
        
        #operator_set의 경우 인덱스를 0부터 쓴다.
        #따라서 +1을 해줘야 한다.
        #i를 1부터 확인하게 되는데, 이 이유는 operator_set의 0번째는 숫자를 1개만 썼을때이므로 이런 경우는 이미 맨처음 N==number 이 구문에서 걸러지기 때문이다.
        if number in operator_set[i]:
            return i+1

    #반복문을 다 돌때까지 없었다면 8보다 크다고 생각하고 -1
    return -1


if __name__ == "__main__":
    N = 5
    number = 12
    solution(N,number)
    # assert solution(N,number) == 4

    # N = 2
    # number = 11
    # assert solution(N,number) == 3