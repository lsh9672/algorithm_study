#백준 1205
import sys


n, new_score, p  = map(int,sys.stdin.readline().split())

if n != 0:
    num_list = list(map(int,sys.stdin.readline().split()))
else:
    print(1)
    exit()

##제일 낮은 점수가 새로운 점수보다 크고, 랭킹에 있는 점수의 수가 랭킹에 올라갈수 있는 수(p)와 같다면 새로 추가할수 없음
if num_list[-1]>= new_score and len(num_list) >= p:
    print(-1)
    
else:
    score_count = 0

    count = 1

    for i in range(len(num_list)-1):
        if num_list[i] <= new_score:
            score_count += count
            print(score_count)
            break
        
        else:
            if num_list[i] < num_list[i+1]:
                score_count += count
                count = 1

            else:
                count += 1
    
    else:
        if num_list[-1] > new_score:
            print(len(num_list)+1)
        else:
            print(len(num_list))
