#백준 2257번 (자료구조,실버2)
import sys

chemical_formula = sys.stdin.readline().strip()


stack = list()

chemical_dict = {"H":1,"C":12,"O":16}

for i in chemical_formula:


    if i == "(":
        stack.append(i)

    elif i.isalpha():
        stack.append(chemical_dict[i])
        
    elif i == ")":
        temp = 0
        while stack[-1] != "(":

            temp_chemical = stack.pop()

            temp+= temp_chemical
        
        stack.pop()
        stack.append(temp)
    
    else:
        stack.append(stack.pop()* int(i))

print(sum(stack))
