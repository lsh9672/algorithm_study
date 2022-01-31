#백준 1010 다리놓기(dp)
import sys


'''입력'''
#테스트 케이스
test_case = int(sys.stdin.readline())


#결과 값 리스트
result = list()

# 사이트 수 => 서쪽:n, 동쪽:m
for _ in range(test_case):
    n,m = map(int,sys.stdin.readline().split())

    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    
    for i in range(n+1):
        for j in range(m+1):

            if i == j:
                dp[i][j] = 1
            
            elif i==1:
                dp[i][j] = j
            
            elif i < j:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
            
            else:
                pass
    
    result.append(dp[n][m])

#출력
for a in result:
    print(a)



    

