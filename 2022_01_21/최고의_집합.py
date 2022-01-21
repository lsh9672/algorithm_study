#프로그래머스 레벨3 - 최고의 집합
#각 원소의 곱이 최대가 되려면 표준편차가 작아야된다. - 즉 곱하는 숫자끼리 차이가 크지 않아야 곱했을때 가장 큰수가 나오게 된다.
# from itertools import combinations_with_replacement as cwr

'''중복조합으로 풀었을 경우
#리스트 곱 구해주는 함수(정렬 커스텀을 위해서)
def mul_list(tuple_input:tuple) -> int:

    result = 1
    for i in tuple_input:
        result *= i

    return result

def solution(n, s):
    answer = []

    #n이 s보다 크면 최고의 집합을 만들수 없음 - 가장 작은 경우가 n이기 때문에
    if n > s:
        return [-1]

    #n이 1이면 계산필요없이 s가 답임
    if n == 1:
        return [s]

    #중복조합을 이용해서 모든 경우의 수 구하기
    #n이 2보다 클때부터 계산
    temp = cwr(range(1,s-n),n)
    temp_list = list()
    for i in temp:
        if sum(i) == s:
            temp_list.append(i)

    #리스트 값들을 곱했을때 가장 큰 순으로 정렬
    temp_list = sorted(temp_list, key = lambda x : mul_list(x),reverse=True)
    answer = sorted(temp_list[0])

    return list(answer)
'''
#각 원소들의 차이가 크지 않아야 곱이 최대가 된다는 아이디어를 이용(구글링 참고)
def solution(n, s):

    #n이 s보다 크면 최고의 집합을 만들수 없음 - 가장 작은 경우가 n이기 때문에
    if n > s:
        return [-1]

    #s를 n으로 나눈 몫을 n번만큼 리스트에 저장한다
    #나온 n개의 숫자를 더하고 s와 비교해서 부족하면(더한값 < s) 조건을 맞추기 위해 부족한 값만큼 균등하게 나눠준다.
    temp = s // n
    
    #리스트에 저장
    temp_list = [temp] * n

    #목표치인 s보다 부족한 값 - 딱떨어지거나 부족함(소수점부분을 버리기 때문에)
    leak_value = s - sum(temp_list)

    #부족한 수만큼 반복하면서 인덱스에 1씩더하므로써 균등하게 만듦
    for i in range(leak_value):
        temp_list[len(temp_list)-1 - i] += 1
        
    return temp_list
    


if __name__ == "__main__":
    n = 2
    s = 9
    print(solution(n,s))
    assert solution(n,s) == [4,5]

    n = 2
    s = 1
    assert solution(n,s) == [-1]

    n = 2
    s = 8
    assert solution(n,s) == [4,4]