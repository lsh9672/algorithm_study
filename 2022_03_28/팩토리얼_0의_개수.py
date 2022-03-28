#백준  1676번 (구현연습)
import sys


n = int(sys.stdin.readline().strip())

n_fac  = 1

for i in range(1,n+1):
    n_fac *= i

n_fac = str(n_fac)

result = 0
for i in n_fac[::-1]:
    if i != "0":
        break

    else:
        result += 1

print(result)