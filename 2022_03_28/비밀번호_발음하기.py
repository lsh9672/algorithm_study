#백준 4659번 (문자열 연습)
import sys

vowel = ["a","e","i","o","u"]

result = list()

while True:
    passwd = sys.stdin.readline().strip()

    if passwd == "end":
        break

    #1. a,e,i,o,u 하나를 반드시 포함해야됨.
    for i in passwd:
        if i in vowel:
            break
    else:
        result.append([passwd,0])
        continue

    #모음이 3개연속, 또는 자음이 3개 연속 오면 안됨.
    vowel_count = 0
    #자음 세기
    not_vowel_count = 0
    pre_word = ""
    for i in passwd:
        #모음일때
        if i in vowel:
            not_vowel_count = 0
            vowel_count += 1

            if vowel_count == 3:
                result.append([passwd,0])
                break

            #이전 단어와 현재 단어가 같으면,
            if i == pre_word:
                #e나 o인지 확인
                if i == "e" or i == "o":
                    pass
                else:
                    result.append([passwd,0])
                    break
        #자음 일때,
        else:
            vowel_count = 0
            not_vowel_count += 1

            if not_vowel_count == 3:
                result.append([passwd,0])
                break
            #두글자가 같을때
            if i == pre_word:
                result.append([passwd,0])
                break

        #현재단어를 다음 비교를 위해 이전 단어에 넣음
        pre_word = i
    
    else:
        result.append([passwd,1])

for a,b in result:
    if b == 1:
        print(f"<{a}> is acceptable.")
    else:
        print(f"<{a}> is not acceptable.")