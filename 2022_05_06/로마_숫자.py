#백준 2608번 (실버1, 자료구조)
import sys



first_roma = sys.stdin.readline().strip()

second_roma = sys.stdin.readline().strip()

num_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

#작은 글자가 오는경우
except_dict = {"IV": 4, "IX" : 9, "XL" :40, "XC" : 90, "CD": 400, "CM" : 900 }

check_alpha = set(["I","X","C"])

three_alpha = set(["I","X","C","M"])

one_alpha = set(["V","L","D"])



## 첫번째: 로마 -> 숫자 변환
def roma_to_num(roma_num):
    result = 0
    i = 0
    while i< len(roma_num):
        if roma_num[i] in check_alpha:
            temp = roma_num[i:i+2]

            if temp in except_dict:
                result += except_dict[temp]
                i+= 2
                continue
        
        result += num_dict[roma_num[i]]

        i+=1

    return result


result_first = roma_to_num(first_roma) + roma_to_num(second_roma)

## 더한 수를 다시 로마 숫자로
##I, X, C, M 연속해서 3번까지 사용가능

temp = str(result_first).zfill(4)

result_second = ""

for i in range(4):

    temp_num = int(temp[i])
    #천의자리
    if i == 0:
        if temp_num > 0:
            result_second += "M" * temp_num
    
    ## 백의 자리
    elif i == 1:

        if temp_num == 9:
            result_second += "CM"
        
        elif temp_num == 4:
            result_second += "CD"

        else:
            if temp_num >= 5:
                result_second += "D"
                temp_num -= 5
            
            result_second += "C" * temp_num

    ## 십의 자리
    elif i == 2:

        if temp_num == 9:
            result_second += "XC"

        elif temp_num == 4:
            result_second += "XL"

        else:
            if temp_num >= 5:
                result_second += "L"
                temp_num -= 5

            result_second += "X" * temp_num
    
    ## 일의 자리
    elif i == 3:

        if temp_num == 9:
            result_second += "IX"

        elif temp_num == 4:
            result_second += "IV"

        else:
            if temp_num >= 5:
                result_second += "V"
                temp_num -= 5
            result_second += "I"*temp_num 


print(result_first)
print(result_second)