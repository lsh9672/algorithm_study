# 백준 21942 (자료구조, 골드2)
import sys
from collections import defaultdict


temp = list(sys.stdin.readline().split())

## 정보의 수
n = int(temp[0])

## 벌금
f = int(temp[-1])

temp2 = temp[1].split('/')

temp3 = temp2[1].split(":")

l_day = int(temp2[0])
l_hour = int(temp3[0])
l_min = int(temp3[1])

##보기 편하게 전부 분으로 바꿈
return_minute = l_min + (l_hour*60) + (l_day * 24 * 60)

# print(f"test2----------2 {return_minute}")

##각 월을 일에 매칭 - 1,2,3,4,5,6,7,8,9,10,11,12
# month_to_day = [0,31,28,31,30,31,30,31,31,30,31,30,31]
month_to_day = [0,31,59,90,120,151,181,212,243,273,304,334,365]

## 년-월-일을 분으로 바꾸기 (년은 항상 동일하므로 버림)
def month_and_day_to_minute(month_day:str)->int:
    temp = month_day.split("-")
    
    temp_day = month_to_day[int(temp[1])-1] + int(temp[2])

    return temp_day * 24 * 60

##시:분 을 분으로 변경
def hour_and_minute_to_minute(hour_minute:str)->int:
    temp = hour_minute.split(":")

    return int(temp[0]) * 60 + int(temp[1])

##{닉네임 : {물품:시간}}으로 저장할 장부
save_name_item_time = defaultdict(dict)

result = defaultdict(int)


test_list = list()


## 시각(년월일, 시분) , 물품,회원닉네임
for _ in range(n):

    input_info = sys.stdin.readline().strip().split()

    ##대여시간을 분으로 환산
    total_time = month_and_day_to_minute(input_info[0]) + hour_and_minute_to_minute(input_info[1])

    ##부품
    item_name = input_info[2]

    ##닉네임
    nick_name = input_info[3]

    if nick_name not in save_name_item_time:
        save_name_item_time[nick_name][item_name] = total_time

    else:
        if item_name not in save_name_item_time[nick_name]:
            save_name_item_time[nick_name][item_name] = total_time

        else:
            temp_save_time = total_time - save_name_item_time[nick_name][item_name]

            ##대여시간을 준수하지 않았다면,
            if return_minute < temp_save_time:
                # print(f"test--------------{temp_save_time - return_minute}")
                result[nick_name] += ((temp_save_time - return_minute)*f)
            
            del save_name_item_time[nick_name][item_name]

    test_list.append([nick_name,item_name,total_time])


if len(result) == 0:
    print(-1)
else:
    temp_items = list(result.items())
    temp_items.sort()
    for result_name, result_money in temp_items:
        print(result_name,result_money)