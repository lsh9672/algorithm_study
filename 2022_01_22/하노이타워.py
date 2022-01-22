#프로그래머스 level 3 - 하노이타워



def hanoi_move(n:int,start:int,end:int,assistant:int,answer:list) -> list:
    print(f"n : {n},start : {start},end : {end},assistant : {assistant}")
    print(f"answer : {answer}")
    
    #1이면 옮길 원반이 한개 남음 -> 목표하는 맨끝으로 옮김
    if n == 1:
        answer.append([start,end])
        print(f"answer1 : {answer}")
    else:
        #1번타워에서 3번타워를 거쳐 2번타워로 이동
        hanoi_move(n-1,start,assistant,end,answer)

        #이동경로 저장
        answer.append([start,end])
        print(f"answer2 : {answer}")
        
        #2번타워에서 1번타워를 거쳐서 3번타워로 이동하게함
        hanoi_move(n-1,assistant,end,start,answer)
        

def solution(n):
    answer = []

    hanoi_move(n,1,3,2,answer)


    return answer

if __name__ == "__main__":

    n = 2
    solution(n)
    # assert solution(n) == [[1,2],[1,3],[2,3]]