#백준 2470번 (골드5, 투포인터)

'''아이디어

전형적인 투포인터 문제이다
만약 모든 값을 일일이 이중반복문으로 탐색하려고 하면, O(n^2)이 나와서 실패하게 된다.
따라서 투포인터를 이용해야 된다.

1. 값을 정렬한다.
2. left포인터 위치는 왼쪽 끝, right 포인터 위치는 오른쪽 끝에 둔다
3. 두 수를 더했는데, 음수라면, left+1을 한다.
4. 반대로 양수라면 right -1을 한다.
5. 0이라면 그대로 출력하고, left>= right가 되면 출력한다.

절대값으로 비교하면서 확인한다 - 절댓값은 0으로 부터 떨어진 거리를 의미하기 떄문
'''
import sys

n = int(sys.stdin.readline())

num_list = list(map(int,sys.stdin.readline().split()))

num_list.sort()

left = 0

right = n-1

result_left = left

result_right = right

result_cal = num_list[left] + num_list[right]



while left < right:

    temp = num_list[left] + num_list[right]

    if abs(temp) < abs(result_cal):

        result_left = left
        result_right = right

        result_cal = temp

        if result_cal == 0:
            break

    if temp < 0:
        left += 1

    elif temp > 0:
        right -= 1


print(num_list[result_left],num_list[result_right])

