#백준 17609번 (문자열, 실버1)
import sys

#입력 - 테스트 케이스의 갯수를 입력한다.
t = int(sys.stdin.readline().strip())

result = list()

for _ in range(t):
    temp = sys.stdin.readline().strip()  

    left_status = True
    right_status = True

    #반복문을 돌면서 한쪽은 앞에서 한쪽은 뒤에서 가운데로 오면서 비교한다.
    for i in range(len(temp)//2):
        #탐색중에 같지 않으면
        if temp[i] != temp[len(temp)-1-i]:

            #왼쪽 단어 무시하고 다음 단어부터 계속 진행해봄
            for x in range(i,len(temp)//2):
                #왼쪽 다음 글자부터 진행했는데도 다르다면 잠깐 체크해두기(오른쪽을 지우고 진행했을때도 안되는지 확인.)
                if temp[x+1] != temp[len(temp)-1-x]:
                    left_status = False
            
            #오른쪽의 단어를 무시하고 계속 진행해봄
            for y in range(i, len(temp)//2):
                
                #오른쪽 글자부터 진행해봤는데도 문제가 있다면, 체크해둠
                if temp[y] != temp[len(temp)-2-y]:
                    right_status = False

            
            #왼쪽을 지워도 안되고 오른쪽을 지워도 안된다면, 회문이 아님
            if left_status == False and right_status == False:
                result.append(2)
                break
            #둘중 하나를 지웠을떄 된다면, 유사 회문임
            elif left_status == True or right_status == True:
                result.append(1)
                break
    
    #둘다 지우지 않아도 된다면 회문임
    else:
        result.append(0)

for i in result:
    print(i)
