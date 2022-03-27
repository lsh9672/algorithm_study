#백준 6550번 (문자열 실버5)
import sys

result = list()

#입력
while True:
    #입력으로 들어오는 문자열이 없으면 종료
    input_value = sys.stdin.readline().strip()

    if not input_value: 
        break

    s,t = input_value.split(" ")

#s가 t의 부분 문자열이 되려면,  문자열 길이가 s<t가 되어야 한다.
    if len(s) > len(t):
        result.append("No")
#len(s) == len(t) 이면 s==t인지 확인하고 아니면 No
    elif len(s) == len(t):
        if s == t:
            result.append("Yes")
        else:
            result.append("No")

# len(s) < len(t)이면, 반복문으로 s와 t의 인덱스를 하나씩 증가시키면서, t에 s의 문자가 있는지 확인
    else:
        count = 0
        for i in s:
            for j in range(count,len(t)):
                if i == t[j]:
                    count = j+1
                    break
            else:
                result.append("No")
                break
        
        else:
            result.append("Yes")
        

for i in result:
    print(i)