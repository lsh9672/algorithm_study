#백준 17140번
import sys


##x,y좌표, 값
r,c,k = map(int,sys.stdin.readline().split())

array_a = list()

for _ in range(3):
    array_a.append(list(map(int,sys.stdin.readline().split())))

'''풀이
1. 문제에서는 나온 횟수가 오름차순이 되도록 정렬하고, 같다면, 해당 숫자가 오름차순이 되도록 정렬하라고 했다.
2. 정렬은 [숫자, 나온 횟수] 이와 같이 리스트로 묶고, lambda를 이용해서 정렬해주면 문제가 해결된다.
3. 이렇게 정렬을 했으면, 리스트의 덧셈연산으로 하나의 리스트로 만들어준다.
4. 이렇게 정렬이 끝나면, 가장 긴 행을 기준으로 해서 나머지 행들에 부족한 부분은 0으로 채워 넣는다.
'''

time = 0

result = -1

#주어진 위치의 값이 k인지 확인
if (0<= r-1 < len(array_a)) and (0<= c-1 < len(array_a[0])) and array_a[r-1][c-1] == k:
    result = time

else:
    ##100초까지 반복
    while time <= 100:

        
        '''R연산'''
        ##1. 행 >= 열 인지 확인
        ##2. 맞다면,정렬
        ##3. 정렬이 끝나면 각 행중 가장 길어진 행의 길이에 맞춰서 나머지 행들도 0을 채워 넣음
        
        if len(array_a) >= len(array_a[0]):
            ##반복문을 돌면서 각각의 수와 횟수를 저장하고, 이를 리스트로 묶고, 정렬한다.
            ##정렬후에는 하나의 리스트안에 넣어준다.
            ## 행의 최대 길이 계산
            time += 1

            temp_max = 0 

            for i in range(len(array_a)):
                temp = dict()

                for j in range(len(array_a[i])):
                    if array_a[i][j] != 0:
                        if array_a[i][j] in temp:
                            temp[array_a[i][j]] += 1
                        
                        else:
                            temp[array_a[i][j]] = 1

                temp_list = list(temp.items())
                temp_list = sorted(temp_list, key=lambda x: (x[1],x[0]))

                temp_sort_list = list()
                
                for arr in temp_list:
                    temp_sort_list += list(arr)

                temp_max = max(temp_max,len(temp_sort_list))
                
                ##정렬된 결과를 다시 리스트에 넣음
                array_a[i] = temp_sort_list
                
            ##각 과정이 끝나면, 가장 긴 열을 기준으로 이 보다 짧은 행은 0으로 채움
            for x in range(len(array_a)):
                ##최대 열의 길이보다 작으면 0을 그만큼 채워넣음
                if len(array_a[x]) < temp_max:
                    array_a[x] += [0] * (temp_max - len(array_a[x]))

            ## R연산은 각 행의 열개수를 늘리는 연산이므로 이 열이 100을 넘었는지 확인
            if temp_max > 100:
                temp_max = 100
                for p in len(array_a):
                    array_a[p] = array_a[p][:100]
                    

        #주어진 위치의 값이 k인지 확인
        if (0<= r-1 < len(array_a)) and (0<= c-1 < len(array_a[0])) and array_a[r-1][c-1] == k:
            result = time
            break
        
         
        
        '''C연산'''
        ##1. 행 < 열 인지 확인
        ##2. 맞다면 정렬
        ##3. 정렬이 끝나면 각 행중 가장 길어진 행의 길이에 맞춰서 나머지 행들도 0을 채워 넣음
        if len(array_a) < len(array_a[0]):

            time += 1

            temp_array_a = list()

            ##최대 열을 구하기 위해
            temp_max = 0


            for i in range(len(array_a[0])):
                temp = dict()

                for j in range(len(array_a)):
                    if array_a[j][i] != 0:
                        if array_a[j][i] in temp:
                            temp[array_a[j][i]] += 1
                        
                        else:
                            temp[array_a[j][i]] = 1

                temp_list = list(temp.items())
                temp_list = sorted(temp_list, key=lambda x: (x[1],x[0]))

                temp_append_list = list()
                for temp_sort in temp_list:
                    temp_append_list += temp_sort

                temp_max = max(temp_max,len(temp_append_list))

                
                temp_array_a.append(temp_append_list)
            
            ## 아래에서 업데이트를 위해 최대 길이만큼 0을 채워넣기
            for x in range(len(temp_array_a)):
                if temp_max > len(temp_array_a[x]):
                    temp_array_a[x] += [0] * (temp_max - len(temp_array_a[x]))

            ## C연산은 각 열의 행개수를 늘리는 연산이므로 이 행이 100을 넘었는지 확인
            if temp_max > 100:
                temp_max = 100
                for p in range(len(temp_array_a)):
                    temp_array_a[p] = temp_array_a[p][:100]


            ##배열 0으로 재정의
            array_a = [[0 for _ in range(len(temp_array_a))] for _ in range(temp_max)]


            ## 초기화한 배열 채우기
            for x in range(len(temp_array_a)):
                for y in range(temp_max):
                    array_a[y][x] = temp_array_a[x][y]

        #주어진 위치의 값이 k인지 확인
        if (0<= r-1 < len(array_a)) and (0<= c-1 < len(array_a[0])) and array_a[r-1][c-1] == k:
            result = time
            break

print(result)