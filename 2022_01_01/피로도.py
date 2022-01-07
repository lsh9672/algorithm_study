#프로그래머스 level2 피로도
from itertools import permutations


#던전을 돈 횟수 계산 함수
def fatigue_calculate(dungeons_list: list,fatigue:int) -> int:
    count =0
    for dungeon in dungeons_list:

        #요구 피로도와 소모피로도
        required_fatigue, consumed_fatigue = dungeon
        
        #요구 피로도가 가지고 있는 피로도보다 적다면 던전을 돈다
        if required_fatigue <= fatigue:
            fatigue -= consumed_fatigue
            count+=1
            
        else:
            pass
        
    return count

def solution(k, dungeons):
    answer = -1
    
    #모든 경우의 던전 순서(순열 이용)
    for i in permutations(dungeons,len(dungeons)):
        temp_fatigue = k
    
        result_dungeon_count = fatigue_calculate(i,temp_fatigue)
        
        #계산한 결과중 가장 큰값(가장많이 돈 횟수)을 저장
        if answer < result_dungeon_count:
            answer = result_dungeon_count

    return answer

if __name__ == "__main__":
    k= 80
    dungeons=[[80,20],[50,40],[30,10]]
    assert solution(k,dungeons) == 3