#백준 1342번 (문자열 연습) - 백트래킹을 이용해서 푸는 것이 좋음
import sys


s = sys.stdin.readline().strip()

#a~z까지 문자의 개수를 저장할 리스트
char_list = [0 for _ in range(26)]

total_length = len(s)

#정답 - 문자열 개수
result = 0

#주어진 문자열에서 문자를 중복없이 저장. - 여기서 하나씩 문자를 꺼내고, char_list를 조회해서 해당 문자를 쓸수 있는지 없는지 판단
char_set = set()

#파라미터로 문자열의 길이와 이어붙일수 있는 빈 문자열을 전달받음
#문자열의 길이는, 주어진 문자길이와 동일해지면, 재귀를 멈추도록 하기 위해서임
def dfs(string_length:int, string_save:str):

    global result
    if total_length == string_length:
        #끝까지 올동안 종료가 안되었다는 것은, 정답이라는 뜻
        result += 1
        return 
    
    #모아둔 알파벳 집합에서 하나씩 꺼내서 문자열을 만듦
    for x in char_set:
        index = ord(x) - ord('a')
        #문자개수를 세는 리스트를 조회해서 해당 문자가 있는 지 확인
        if char_list[index] == 0:
            continue
            
        #새로 이어 붙일 문자가 이전 문자와 동일하다면,
        if len(string_save) >= 1 and x == string_save[-1]:
            continue
            
        char_list[index] -= 1
        dfs(string_length+1,string_save + x)
        char_list[index] += 1


for i in s:
    index = ord(i) - ord('a')
    char_list[index] += 1
    char_set.add(i)

dfs(0,"")
print(result)






