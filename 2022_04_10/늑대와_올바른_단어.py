#백준 13022 (늑대와 올바른 단어)
import sys


input_value = sys.stdin.readline().strip()


def value_count_check(value_count:dict,format:str) -> bool:

    if format == "wolf" and value_count["w"] == value_count["o"] == value_count["l"] == value_count["f"]:
        return True

    return False




def solution() -> int:

    value_count = {"w":0,"o":0,"l":0,"f":0}

    #시작이 w가 아니면 잘못된것
    if input_value[0] != "w":
        return 0

    #길이가 4글자가 안넘으면 잘못된것
    if len(input_value)<4:
        return 0
    
    format_check = input_value[0]
    value_count[format_check] = 1

    for i in range(1,len(input_value)):
        
        if format_check[-1] != input_value[i]:
            #이전 문자가 f라면
            if format_check[-1] == "f":
                #현재까지 저장한 알파벳 개수를 확인해봄
                if value_count_check(value_count,format_check) == True:
                    value_count = {"w":0,"o":0,"l":0,"f":0}
                    format_check = input_value[i]
                    #새로운 값으로 업데이트 하고나서 w인지 확인
                    if format_check != "w":
                        return 0
                
                else:
                
                    return 0
            else:
                format_check += input_value[i]
        
        value_count[input_value[i]] += 1
        

    #중간에 리턴없이 끝까지 왔으면 한번더 확인        
    else:
        if value_count_check(value_count,format_check) == True:
            return 1
    
    return 0

print(solution())