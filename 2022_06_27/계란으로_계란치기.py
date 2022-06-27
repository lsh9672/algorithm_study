##백준 16987 (백트래킹, 실1)
import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().strip())

s_list = list()
w_list = list()

for _ in range(n):
    ## S , W
    s,w = map(int,sys.stdin.readline().split())
    s_list.append(s)
    w_list.append(w)

result = 0


def recursive(index:int, temp_egg:list, count:int):
    global result

    if index == len(temp_egg):
        result = max(result,count)
        return
    
    if temp_egg[index] <= 0:
        recursive(index+1,temp_egg,count)

    else:
        check = True
        for i in range(len(temp_egg)):
            
            if i != index and temp_egg[i] > 0:
                check = False
                temp_count= 0

                # temp1 = temp_egg[index]
                # temp2 = temp_egg[i]
                temp_egg_copy = temp_egg[:]


                temp_egg_copy[index] -= w_list[i]
                temp_egg_copy[i] -= w_list[index]
                
                if temp_egg_copy[index] <= 0:
                    temp_count+=1

                if temp_egg_copy[i] <= 0:
                    temp_count+=1

                print(f"test_egg : {temp_egg}")
                recursive(index+1, temp_egg_copy,count+temp_count)

        if check == True:
            recursive(index+1,temp_egg,count)

recursive(0,s_list,0)

print(result)