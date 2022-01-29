#프로그래머스 level 3 - 거스름돈
#dp

#dp같지 않은 풀이
def solution(n, money):
    answer = 0

    dp = [0] * (n+1)
    dp[0] = 1
    #주어지는 화폐가 정렬안되어있을 수도 있으니 정렬
    money.sort()


    for coin in money:
        for i in range(coin,n+1):
            dp[i] += dp[i-coin]

    
    return dp[n]%1000000007


if __name__ == "__main__":

    n = 5

    coin = [1,2,5]

    print(solution(n,coin))