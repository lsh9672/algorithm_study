#SWEA 4698번 (싸피,d3)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_20/sample_input (9).txt", "r")


T = int(input())


def find_prime_num(num):
    prime_list = [True] * (num+1)
    prime_list[0] = False
    prime_list[1] = False

    for i in range(2,int(num**0.5)):
        if prime_list[i] == True:
            for j in range(2*i,num+1,i):
                prime_list[j] = False
    
    return prime_list

prime_list = find_prime_num(10**6)

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    d,a,b = map(int,sys.stdin.readline().split())

    result = 0

    for i in range(a,b+1):
        if prime_list[i] == True and str(d) in str(i):
            result +=1

    print(f"#{test_case} {result}")