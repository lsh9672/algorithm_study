#SWEA - d2

# n - (n-1) - (n-1) - (n-2) - (n-2) - (n-3) - (n-3) - (1) - (1)
# 방향 : (0,1),(1,0),(0,-1),(-1,0)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    dir = [[0,1],[1,0],[0,-1],[-1,0]]

    n = int(input())

    temp_result= [[0 for _ in range(n)] for _ in range(n)]

    dir_count = 0

    count = 1

    current_x, current_y = 0,0

    temp_list = [n-1]

    for i in range(1,n):
        temp_list.append(n-i)
        temp_list.append(n-i)

    temp_result[current_x][current_y] = count
    
    for a in temp_list:
        for _ in range(a):
            count += 1
            current_x = current_x + dir[dir_count%4][0]
            current_y = current_y + dir[dir_count%4][1]
            temp_result[current_x][current_y] = count

        
        dir_count += 1

    print(f"#{test_case}")
    for k in range(n):
        print(*temp_result[k])
