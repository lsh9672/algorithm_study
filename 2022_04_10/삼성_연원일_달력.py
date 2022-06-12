import sys



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다



for test_case in range(1, T + 1):
    temp = input().strip()

    month_list = set([4,6,9,11])

    result = ""

    if len(temp) != 8:
        print(f"#{test_case} {-1}")
        continue
    
    year = temp[:4]
    month = temp[4:6]
    day = temp[6:]

    if year == "0000":
        print(f"#{test_case} {-1}")
    
    elif int(month) <=0 or int(month) > 12:
        print(f"#{test_case} {-1}")
    
    elif int(day) <= 0 or int(day) > 31:
        print(f"#{test_case} {-1}")

    elif int(month) == 2 and int(day) > 28:
        print(f"#{test_case} {-1}")
    
    elif (int(month) in month_list) and int(day) >30:
        print(f"#{test_case} {-1}")
    
    else:
        print(f"#{test_case} {year}/{month}/{day}")

    
