##백준 16165번 (자료구조 연습., 실버3)
import sys
from collections import defaultdict

n,m = map(int,sys.stdin.readline().split())

result = list()

team_dict = defaultdict(list)
member_dict = dict()

for _ in range(n):
    team_name = sys.stdin.readline().strip()

    num = int(sys.stdin.readline())

    for _ in range(num):
        temp_member_name = sys.stdin.readline().strip()
        team_dict[team_name].append(temp_member_name)
        member_dict[temp_member_name] = team_name

# print(team_dict.keys())
# print("-----",list(member_dict.items()))

for _ in range(m):
    test_name = sys.stdin.readline().strip()
    test_type = int(sys.stdin.readline().strip())

    if test_type == 0:
        team_dict[test_name].sort()
        for i in team_dict[test_name]:
            result.append(i)
            # print(i)
    
    else:
        # print(member_dict[temp_member_name])
        result.append(member_dict[test_name])

for i in result:
    print(i)


