#SWEA 1974번 (싸피, D2)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_05/input (14).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 1

    graph = list()

    for _ in range(9):
        graph.append(list(map(int,sys.stdin.readline().split())))

    check = True

    
    
    for i in range(9):
        ##1.가로줄 확인
        if len(set(graph[i])) != 9:
            check = False
            result = 0
            break
        ##2 세로줄확인
        temp = set()
        for j in range(9):
            temp.add(graph[j][i])
        
        if len(temp) != 9:
            result = 0
            break
            

    if check == True:
        ##3. 각 칸
        for_check = True
        for i in range(0,7,3):
            for j in range(0,7,3):
                temp = set()
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        temp.add(graph[x][y])
                
                if len(temp) != 9:
                    result = 0
                    for_check=False
                    break
            
            if for_check== False:
                break


    print(f"#{test_case} {result}")