#백준 5554번 (스트릭 유지 - 면접때문에)
import sys

total = 0

for _ in range(4):

    total += int(sys.stdin.readline().strip())

result_minute = total//60

result_second = total%60

print(result_minute)
print(result_second)
