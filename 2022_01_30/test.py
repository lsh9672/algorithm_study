import sys


#입력
num = list(map(int,sys.stdin.readline().split()))

#오름차순 정렬했을때 그대로이면 ascending
if num == sorted(num):
    sys.stdout.write("ascending")

#내림차순 정렬했을떄 그대로이면 descending
elif num == sorted(num,reverse=True):
    sys.stdout.write("descending")

#오름차순, 내림차순 했을떄 둘다 아니면 mixed
else:
    sys.stdout.write("mixed")