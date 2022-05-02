#SWEA 1946번 (싸피,D2)
import sys

sys.stdin = open("/home/leesh/lsh/my_study/algorism_study/2022_05_02/input (6).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    n = int(sys.stdin.readline().strip())
    

    result = ""

    temp_str = ""
    for _ in range(n):
        word, count = sys.stdin.readline().split()

        count = int(count)

        
        
        for _ in range(count):
            temp_str += word

            if len(temp_str) == 10:
                temp_str += "\n"
                result += temp_str
                temp_str = ""
        
    
    result += temp_str
        
    print(f"#{test_case}")
    print(result.strip())