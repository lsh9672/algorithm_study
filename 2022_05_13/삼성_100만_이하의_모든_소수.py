
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

n = 10**6

num_list = [True] * (n+1)

result = list()

m = int(n**0.5)
for i in range(2,m+1):
    if num_list[i] == True:
        for j in range(i+i,n+1,i):
            num_list[j] = False

for i in range(2, n+1):
    if num_list[i] == True:
        print(i, end = " ")
