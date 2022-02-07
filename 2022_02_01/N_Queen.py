#프로그래머스 N-Queen(백트래킹)
#백트래킹은 DFS에서 정답이 아닐것같은 부분을 가지치기해서 탐색경우를 줄이는 일종의 전략이다


#현재상태가 조건을 만족하는지(퀸이 서로 공격을 할수 없는지) 체크하는 함수
#False면 조건을 만족하지 않음
def check(queen:list,row:int)->bool:
    #주어진 row => 좌표상 맨위(row가 0) 부터 하나씩 차근차근 채워내려가기 때문에 주어진 row를 인덱스로 하는 queen의 값이 최근에 추가된 퀸의 위치
    #따라서 0부터 해당 row까지 비교하면서 서로 공격할수 있는 위치인지 확인
    #퀸은 가로세로 대각선으로 이동이 가능하다.
    for i in range(row):
        #queen리스트에서 i번째와 row번째가 같으면 동일 컬럼에 있기 떄문에 퀸이 서로 공격가능, 즉 놓을수 없음
        #row-i => 두 좌표의 세로로 떨어진 정도 , queen[row] - queen[i] => 두 좌표의 가로로 떨어진 정도 
        #위의 두 값이 같으면 같은 대각선상에 있음, 예를 들면 (1,1) (3,3)은 가로,세로가 각각 2씩 떨어져 있다. 즉 같은 대각선 상에 있음
        #row-i=> 이경우는 항상 row가 크거나 i와 같기 때문에 그대로 빼면되지만, queen[row] - queen[i] 이 경우는 row인덱스의 위치가 더 왼쪽에 있으면 음수가 나옴
        #따라서 절댓값을 취해줌
        if queen[i] == queen[row] or abs(queen[row]-queen[i]) == row-i:
            return False
    return True

    



#재귀함수 - 각 경우에 대해서 탐색하는 함수
def bfs(queen:list,row:int) -> int:
    length = len(queen)
    #배치할 퀸의 개수 카운트
    count = 0

    #계속탐색하다 탐색하는 row가 좌표평면의 끝에 도달하면 종료
    if length == row:
        return 1
        
    #좌표평면의 끝이 아니면 row+1 해서 자기 자신호출에서 탐색을 계속 함
    for i in range(length):
        #퀸을 주어진 row에서 컬럼을 바꿔가면서 넣어봄
        queen[row] = i
        #퀸을 넣어보고 check함수를 돌려서 조건에 맞게 퀸이 안겹치는지 확인
        if check(queen,row):
            #조거네 맞으면 row를 하나 증가시켜서 반복하고 발새한 count값을 계속 더함
            count+=bfs(queen,row+1)
    
    return count


def solution(n:int)->int:
    #퀸의 위치를 담을 리스트 - 같은 row에는 하나의 퀸밖에 올수 없어서 인덱스를 row으로 함, 
    #예를들어 [1,2,3,4]이면 (0,1),(1,2),(2,3),(3,4) => 같은 row에는 어차피 퀸이 하나 밖에 오지못함
    queen_location = [0]*n

    #0번째 row부터 시작하기 떄문에 row 위치에 0을 넣음
    answer = bfs(queen=queen_location,row=0)

    return answer


if __name__=="__main__":
    n=4
    assert solution(n) == 2


    