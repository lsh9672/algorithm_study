#백준 1759번 (암호만들기, 골드5)
import sys


l,c = map(int,sys.stdin.readline().split())

alpha_list = list(sys.stdin.readline().split())

alpha_list.sort()

vowel_set = {"a","i","o","u","e"}

def back_tracking(result:list,start_index:int)->None:
    global vowel_set
    ##글자 길이가 목표길이면 모음 1개이상, 자음 2개이상 존재하는지 확인

    if len(result) == l:
        vowel_count = 0
        consonant_count = 0

        for temp in result:
            if temp in vowel_set:
                vowel_count += 1
            else:
                consonant_count += 1

            if vowel_count >= 1 and consonant_count >=2:
                print("".join(result))
                break
        return

    ## 남은 값들로 길이 l을 만들수 없으면 리턴
    if len(result) + (c - start_index) < l:
        return 

    for i in range(start_index,c):
        result.append(alpha_list[i])
        back_tracking(result,i+1)
        result.pop()



back_tracking(list(),0)