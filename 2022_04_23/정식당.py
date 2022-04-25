# 백준 17479번(자료구조 연습)
import sys
from collections import defaultdict


##일반, 특별, 서비스
a,b,c = map(int, sys.stdin.readline().split())

normal_menu = dict()

specify_menu = dict()

service_menu = set()


for _ in range(a):
    menu, price = sys.stdin.readline().split()

    normal_menu[menu] = int(price)

for _ in range(b):
    menu, price = sys.stdin.readline().split()

    specify_menu[menu] = int(price)

for _ in range(c):
    menu = sys.stdin.readline().strip()
    service_menu.add(menu)


##주문
order_num = int(sys.stdin.readline())

current_normal_price = 0
current_specify_price = 0

current_specify_count = 0

current_service_count = 0

temp_service_menu = list()

for _ in range(order_num):
    order_menu = sys.stdin.readline().strip()

    if order_menu in normal_menu.keys():
        current_normal_price += normal_menu[order_menu]

    elif order_menu in specify_menu.keys():
        current_specify_price += specify_menu[order_menu]
        current_specify_count += 1

    elif order_menu in service_menu:
        current_service_count+=1

## 서비스 메뉴가 제대로 되었는지 확인

result = "Okay"
if current_normal_price < 20000 and current_specify_count > 0:
    result = "No"

elif current_service_count > 2:
    result = "No"

elif current_normal_price+current_specify_price < 50000 and current_service_count >= 1:
    result = "No"

print(result)
