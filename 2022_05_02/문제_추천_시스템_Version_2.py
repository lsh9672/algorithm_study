#백준 21944번 (자료구조 연습,골드3)
''' 매번 정렬해서 찾는 방법은 정렬이 O(nlogn)이므로 오래걸림,
따라서 max,min으로 찾아야되는데, 난이도가 같을때는 문제번호를 비교해야 되기 때문에,
그냥 max를 할수 없음
이 두 수를 합쳐서 크기를 구분할수 있게 해야되는데, 그냥 두수를 더하면, 난이도는 100까지이고 문제번호는 10만까지이므로
난이도가 낮은데 문제번호가 높은 경우 우선순우가 뒤틀릴수 있음
따라서 난이도 가 문제번호에 영향을 끼지치 않도록 10만을 곱해서 더하여 비교하는 방법을 취함.
나중에 문제번호 복구는 10만으로 나눈 나머지에 +1해서 구하면 됨
'''

import sys
from collections import defaultdict

## 문제번호: P, 난이도:L, 알고리즘 분류: G
n = int(sys.stdin.readline())

recommend1_dict = defaultdict(dict)
recommend2_dict = defaultdict(dict)
recommend3_dict = defaultdict(dict)
solve_dict = dict()

for _ in range(n):

    temp_p, temp_l,temp_g = map(int,sys.stdin.readline().split())

    cal_temp = 100000*temp_l + (temp_p -1)

    ## 추천1번 기능에서 사용할 딕셔너리 - 어려운문제의 구분은 items로 key,value뽑아서 정렬해서 구함.
    recommend1_dict[temp_g][cal_temp] = 1

    ## 추천2번 기능에서 사용할 딕셔너리
    recommend2_dict[temp_p] = cal_temp
    ##추천 3번 기능에서 사용할 딕셔너리
    recommend3_dict[temp_l][temp_p] = 1

    ## 삭제시에 계산해서 저장한 cal_temp 찾기위해 저장해둠
    solve_dict[temp_p] = [temp_g,temp_l]


m = int(sys.stdin.readline())

result = list()


for _ in range(m):
    temp = sys.stdin.readline().split()

    if temp[0] == "recommend":
        g = int(temp[1])


        ##알고리즘이 g이고, 그 중 난이도(L)이 가장 높은 문제
        if temp[2] == "1":
            # result.append(max(recommend1_dict[g].keys()))
            print(max(recommend1_dict[g].keys())%100000 + 1)
        
        ##알고리즘이 g이고, 그 중 난이도(L)이 가장 낮은 문제
        elif temp[2] == "-1":
            # result.append(min(recommend1_dict[g].keys()))
            print(min(recommend1_dict[g].keys())%100000 + 1)


    elif temp[0] == "recommend2":
        ##난이도(L)이 가장 높은 문제 
        if temp[1] == "1":
            # result.append(max(recommend2_dict.values()))
            print(max(recommend2_dict.values())%100000 + 1)
        ##난이도(L)이 가장 낮은 문제
        elif temp[1] == "-1":
            # result.append(min(recommend2_dict.values()))
            print(min(recommend2_dict.values())%100000 + 1)

    elif temp[0] == "recommend3":
        l = int(temp[2])

        check = int(temp[1])
        temp_result = -1
        ##난이도(L)보다 크거나 같은 문제중 가장 쉬운 문제 번호 출력
        if check == -1:
            l += check
        
        while 0<= l <= 100:
            if recommend3_dict.get(l):
                if check == 1:
                    temp_result = min(recommend3_dict[l].keys())
        ##난이도(L)보다 낮은 문제중, 가장 어려운 문제 번호 출력
                else:
                    temp_result = max(recommend3_dict[l].keys())
                break

            l += check

        print(temp_result)
    
    elif temp[0] == "add":
        p,l,g, = int(temp[1]),int(temp[2]),int(temp[3])
        cal_value = l * 100000 + (p-1)
        recommend1_dict[g][cal_value] = 1
        recommend2_dict[p] = cal_value
        recommend3_dict[l][p] = 1
        solve_dict[p] = [g,l]


    elif temp[0] == "solved":
        p = int(temp[1])
        
        g,l = solve_dict[p]

        cal_value = l * 100000 + (p-1)

        del recommend1_dict[g][cal_value]
        del recommend2_dict[p]
        del recommend3_dict[l][p]


# for i in result:
#     if i == -1:
#         print(-1)
#     else:
#         print(i%100000 + 1)