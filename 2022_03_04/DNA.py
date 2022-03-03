#백준 1969번 구현 (실버5)
import sys

n,m = map(int,sys.stdin.readline().split())

dna_list = list()

for _ in range(n):
    dna_list.append(sys.stdin.readline().strip())


result_dna = ""

result_count = 0

for i in range(m):
    a,c,g,t = 0,0,0,0

    for j in dna_list:

        if j[i] == "A":
            a+=1

        elif j[i] == "C":
            c+=1
        
        elif j[i] == "G":
            g+=1

        elif j[i] == "T":
            t+=1
        
    #가장 큰값 구하기
    if max(a,c,g,t) == a:
        result_dna += "A"
        result_count += t+g+c

    elif max(a,c,g,t) == c:
        result_dna += "C"
        result_count += a+g+t
    
    elif max(a,c,g,t) == g:
        result_dna += "G"
        result_count += a+t+c

    elif max(a,c,g,t) == t:
        result_dna += "T"
        result_count += a+c+g

print(result_dna)
print(result_count)







