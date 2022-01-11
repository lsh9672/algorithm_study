#백준 1003 피보나치 수열(dp)


call_zero = [1,0,1]
call_one = [0,1,1]

def solution(n:int) -> tuple:
    check_length = len(call_zero)
    #주어진 값이 이미 메모리에 저장되어 있지 않으면 추가해야됨.
    if n >= check_length:
        for i in range(check_length,n+1):
            call_zero.append(call_zero[i-1] + call_zero[i-2])
            call_one.append(call_one[i-1] + call_one[i-2])

    return (call_zero[n],call_one[n])

#몇번 계산할것인지
cal_count = int(input())

for _ in range(cal_count):
    n = int(input())
    zero_count, one_count = solution(n)
    print(f"{zero_count} {one_count}")



# if __name__ =="__main__":
    
    