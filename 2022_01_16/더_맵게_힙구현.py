##프로그래머스 level2 - 더 맵게(수정- 힙으로 이용해서 다시 구현
import heapq

def solution(scoville, K):
    answer = 0

    scoville = sorted(scoville)

    heapq.heapify(scoville)

    if scoville[0]>= K:
        return 0

    #스코빌 지수가 K 미만일 경우
    while True:

        if len(scoville) <= 1:
            answer = -1
            break
        
        #가장 작은 값 출력
        first_scoville = heapq.heappop(scoville)

        #그다음으로 작은 값 출력
        second_scoville = heapq.heappop(scoville)
        temp = first_scoville+(second_scoville*2)

        heapq.heappush(scoville,temp)

        answer += 1

        if scoville[0]>= K:
            break

    return answer


if __name__ == "__main__":
    scoville = [1,2,3,9,10,12]
    K = 7
    assert solution(scoville, K) == 2
    # solution(scoville,K)