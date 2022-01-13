#프로그래머스 level2 H-index
#
def solution(citations):
    answer = 0
    citations = sorted(citations)
    
    for i in range(len(citations)):
        if citations[i] >= len(citations)-i:
            
            return len(citations)-i
    return answer


if __name__ == "__main__":
    citations = [3,0,6,1,5]
    assert solution(citations) == 3