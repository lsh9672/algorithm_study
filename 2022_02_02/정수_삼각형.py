#프로그래머스 level 3 - 정수삼각형(dp문제)
def solution(triangle:list) -> int:
    answer = 0

    #1. 맨위에서 부터 아래로 더해나감
    #2. 더한값을 그대로 저장함
    #3. 더할떄는 옆의 값이 더해졌을때 더 클수도 있으니 비교함
    #4. 가장 마지막줄에 최종적으로 더해진 값들이 있고, 그중에서 가장 큰 값 선택
    
    #삼각형의 높이가 1이면 그대로 출력
    if len(triangle) == 1:
        return triangle[0][0]


    #첫번째 줄 부터 순차적으로 내려가면서 탐색
    for i in range(len(triangle)-1):
        
        #check변수가 True이면 왼쪽에 값을 더하고
        #False이면 왼쪽에 값을 더하지 않음
        #이것을 사용한 이유는 현재 값에서 다음 줄의 오른쪽에 더했을떄 값이 다음 값에서 다음줄의 왼쪽에 더했을떄 값보다 크다면 
        #다음 값은 왼쪽에 더할필요가 없기 때문이다.
        check = True
        #한줄에 있는 값들을 꺼내서 다음 값들에 더함
        for j in range(len(triangle[i])):

            #왼쪽, 즉 인덱스상으로 바로 아래에 더하는 값(+1,0)
            if check == True:
                triangle[i+1][j] += triangle[i][j]

            '''
            오른쪽대각선에 더하는 값(인덱스로 따지면 (+1,+1))
            이경우에는 옆에 있는 값과 비교해야됨
            옆(컬럼+1)에 있는 값이 더 크면 그냥 패스함
            인덱스의 끝이면 멈춤
            '''
            
            #마지막 값이면 그냥 오른쪽에 더하고 아래 연산 실행안하도록 패스
            if j == len(triangle[i])-1:
                triangle[i+1][j+1] += triangle[i][j]
                break

            #오른쪽아래에 더했을때
            temp_right_value = triangle[i+1][j+1] +triangle[i][j]

            #오른쪽값이 왼쪽아래에 더했을때
            temp_next_left_value = triangle[i+1][j+1] + triangle[i][j+1]

            #두 값중에 오른쪽아래에 더한값이 더 크면 check를 False로 만들어서 다음 연산에서 왼쪽에 안더하도록함
            if temp_right_value >= temp_next_left_value:
                triangle[i+1][j+1] = temp_right_value
                check = False

            else:
                check = True

    #제일 마지막줄에 최종적인 숫자의 합이 저장됨
    #이를 정렬하고 제일 뒤의 값 출력(가장 큰수이므로)
    #max를 쓰지 않는 이유는 시간복잡도가 O(n)이고 정렬은 O(nlogn)이다

    result = sorted(triangle[-1])
    
    return result[-1]

#원리는 같지만 좀더 간결하고 빠른 코드
def solution2(triangle:list) -> int:

        #삼각형의 높이가 1이면 그대로 출력
    if len(triangle) == 1:
        return triangle[0][0]

    #첫번째값은 미리 업데이트
    triangle[1][0] += triangle[0][0]
    triangle[1][1] += triangle[0][0]

    for i in range(1,len(triangle)-1):

        for j in range(len(triangle[i])):

            #왼쪽 끝일때
            if j==0:
                triangle[i+1][0] += triangle[i][0]
                triangle[i+1][1] += max(triangle[i][0],triangle[i][1])

            #오른쪽 끝일때
            elif j==(len(triangle[i])-1):
                triangle[i+1][-1] += triangle[i][-1]

            #둘다 아닐때 - 다음값과 비교해서 더큰값을 아래에 더함
            else:
                triangle[i+1][j+1] += max(triangle[i][j],triangle[i][j+1])

    result = sorted(triangle[-1])
    return result[-1]

if __name__=="__main__":

    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    assert solution2(triangle) == 30