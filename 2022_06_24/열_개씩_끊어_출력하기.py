# 백준 11721번 (스트릭 유지)
import sys

input_string = sys.stdin.readline().strip()

string_len = len(input_string)

temp = string_len // 10

if string_len <= 10:
    print(input_string)
else:
    for i in range(temp):
        print(input_string[i*10: i*10 + 10])

    if string_len % 10 != 0:
        print(input_string[(i+1)*10: (i+1) * 10 + 10])