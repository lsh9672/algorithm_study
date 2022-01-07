##프로그래머스 level2 - 더 맵게


def solution(scoville, K):
    answer = 0

    if min(scoville) >= K:
        return 0
    
    #스코빌 지수가 K 미만일 경우
    while min(scoville) < K:

        if len(scoville) <= 1:
            return -1
        first_scoville = min(scoville)
        #가장 안매운 스코빌 지수 값 삭제
        del scoville[scoville.index(first_scoville)]

        second_scoville = min(scoville)
        scoville[scoville.index(second_scoville)] = first_scoville+(second_scoville*2)

        answer += 1

    return answer


if __name__ == "__main__":
    scoville = [1,2,3,9,10,12]
    K = 7
    assert solution(scoville, K) == 2