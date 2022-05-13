#백준 2671번(문자열, 골드5)

import sys
import re

pattern = re.compile("(100+1+|01)+")

input_string = sys.stdin.readline().strip()

temp = re.fullmatch(pattern, input_string)

if temp != None:

    print("SUBMARINE")

else:
    print("NOISE")




