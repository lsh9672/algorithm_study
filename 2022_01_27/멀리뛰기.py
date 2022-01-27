#프로그래머스 level 3 - 멀리뛰기
#DP 문제 - n칸을 뛰는 경우는 n-1칸에서 +1칸하는 경우와 n-2칸에서 +2하는 경우

def solution(n):
    answer = 0
    dp = [0] * (n+1)
    dp[0] = None
    #1칸 뛰는 경우는 (1)
    dp[1] = 1

    if n == 1:
        return dp[1]%1234567
    #2칸뛰는 경우는 (1,1), (2)
    dp[2] = 2

    for i in range(3,n+1):
        dp[i] = (dp[i-1] + dp[i-2])%1234567

    return dp[n]


if __name__ == "__main__":

    n = 1
    assert solution(n) == 1

    n = 4
    assert solution(n) == 5

    n = 3
    assert solution(n) == 3
