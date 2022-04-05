#백준 11053번(스트릭 유지겸, dp연습 - 싸피대비겸 코테 dp유형 적응)

#dp 풀이
import sys


n = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))