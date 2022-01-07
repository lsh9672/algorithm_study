#프로그래머스 level2 조이스틱
#위아래 이동 거리 계산
def up_and_down_distance(alphabet: str) -> int:

    distance = 0
    #위,아래로 이동했을때 각각 몇인지 계산
    #위로 이동했을때 이동거리
    distance_up = abs(ord('A') - ord(alphabet))
    
    #아래로 이동했을때 이동거리
    distance_down = 1+ (ord('Z') - ord(alphabet))

    #더 적게 이동한 쪽 선택
    distance = min(distance_up,distance_down)

    return distance
    

def solution(name):
    answer = 0

    min_distance = len(name) - 1

    for i in range(len(name)):
        #위아래 이동 계산
        answer += up_and_down_distance(name[i])
        #좌,우로 이동했을때 각각 몇인지 계산
        #우로 이동했을때 A이면
        next_location = i + 1
        while next_location < len(name):
            if name[next_location] == "A":
                next_location += 1
            else:
                break
        
        move_left = i + i +len(name) - next_location
        
        min_distance = min(min_distance, move_left)

    answer += min_distance
    return answer

if __name__=="__main__":

    print(f"\ntest2")
    name = "BBABAAAB"
    print(solution(name))