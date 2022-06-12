#백준 12933번
import sys


input_duck = sys.stdin.readline().strip()

str_length = len(input_duck)

visited = [0] * str_length

goal_str = "quack"

duck_count = 0

#글자 수가 5의 배수가 아니면 -1
if str_length%5 != 0:
    print(-1)

else:
    for i in range(str_length):

        # q(시작)이고 방문하지 않았다면, quack을 찾는 탐색 시작
        if input_duck[i] == "q" and visited[i] == 0:

            count = 0
            check = True
            for j in range(i,str_length):
                if input_duck[j] == goal_str[count] and visited[j] == 0:
                    visited[j] = 1
                    if input_duck[j] == "k":
                        if check == True:
                            duck_count += 1
                            check = False
                        count = 0
                        continue
                        
                    count+=1

    if duck_count == 0 or 0 in visited:
        print(-1)

    else:
        print(duck_count)