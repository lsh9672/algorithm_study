#백준 3613 (문자열 연습, 실버 4)
import sys

variable = sys.stdin.readline().strip()

result_value = ""

#언더바가 있으면 C++
if "_" in variable:

    #맨 앞과 맨뒤에 언더바가 있으면 안되고, 언더바가 두개이상 붙어있으면 안됨
    if variable[0] == "_" or  variable[-1] == "_" or "__" in variable:
        print("Error!")
        exit()

    #언더바에 문제가 없으면 소문자인지 체크해야됨.
    else:
        check = False
        for i in variable:
            if i.isupper():
                print("Error!")
                exit()
            #언더바가 나오면 다음 글자를 대문자로 바꿔야됨.
            elif i == "_":
                check = True
                continue
                
            elif check == True:
                check = False
                result_value += i.upper()
                continue
            
            result_value += i


#언더바가 없으면 자바
else:
    #첫글자가 대문자면 에러
    if variable[0].isupper():
        print("Error!")
        exit()
    else:
        for i in variable:
            if i.isupper():
                result_value += "_" + i.lower()
                continue
            result_value += i

print(result_value)
