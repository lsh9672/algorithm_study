## 백준 11365번(스트릭 유지용)

import sys

while True:
    s = sys.stdin.readline().strip()
    
    if s == "END":
        break

    else:
        print(s[::-1])

