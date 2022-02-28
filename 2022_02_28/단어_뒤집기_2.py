#백준 17413번 단어_뒤집기_2 구현
import sys


#입력
word = sys.stdin.readline().strip()

result_word = ""

#False면 문자열을 뒤집음
check = False

temp_word = ""

for i in word:
    if check == False:
        if i == "<":
            check = True
            temp_word += i
        elif i == " ":
            temp_word+=i
            result_word += temp_word
            temp_word = ""
        else:
            temp_word = i + temp_word
    
    #True이면 문자열을 그대로 저장함.
    else:
        temp_word += i
        if i == ">":
            check = False
            result_word += temp_word
            temp_word = ""

result_word += temp_word
print(temp_word)
print(result_word)
