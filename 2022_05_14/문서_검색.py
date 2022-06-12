#백준 1543번 (문자열 , 실버4)
import sys

input_string = sys.stdin.readline().strip()

search_string = sys.stdin.readline().strip()

result = 0

index = 0

while index <= (len(input_string) - len(search_string)):


    if input_string[index] == search_string[0]:
        for i in range(len(search_string)):
            if input_string[index+i] != search_string[i]:
                index += 1
                break
        else:
            index += (i+1)
            result += 1
    else:
        index+= 1



print(result)