#백준 2064 비트마스크
import sys


'''입력'''
n = int(sys.stdin.readline())
total = list()

for _ in range(n):
    a,b,c,d = map(int,sys.stdin.readline().rstrip().split('.'))
    #전부 8자리를 채워서 이진수 변환 
    total.append(format(a,'08b')+format(b,'08b')+format(c,'08b')+format(d,'08b'))

'''연산'''
#반복문을 돌면서 어디까지 같은지 확인
#서브넷 마스크 업데이트할 리스트, 기본은 전부 0
mask = ['0']*32

for i in range(len(total[0])):
    #값 체크를 위해서 넣음
    temp = total[0][i]
    check = True

    for j in total:
        if temp != j[i]:
            check = False
            break
    #전부 같으면 1
    else:
        mask[i] = '1'
    
    if check is False:
        break

#리스트에 있는 것 이어붙여서 문자열로 만듦
mask_str = ''.join(mask)

#주어진 ip주소중에 첫번째것을 가져와서 구한 마스크값과 &연산
ip_str ='0b'+total[0]
network_address_str = format(int(mask_str,2)&int(ip_str,2),'032b')


#8자리씩 끊어서 저장
network_result = list()

mask_result = list()

#8자리씩 끊음
for i in range(4):
    network_result.append(str(int('0b'+network_address_str[i*8:(i*8)+8],2)))
    mask_result.append(str(int('0b'+mask_str[i*8:(i*8)+8],2)))

print('.'.join(network_result))
print('.'.join(mask_result))