#백준 14889번 (삼성기출, 실버2)
import sys
from itertools import combinations

n = int(sys.stdin.readline().strip())

team_member = [i for i in range(1,n+1)]

field = []

for _ in range(n):
    field.append(list(map(int,sys.stdin.readline().split())))

result = 10000

for start_candidate in combinations(team_member,n//2):
    
    start_team = 0
    link_team = 0

    link_candidate = list(set(team_member) - set(start_candidate))

    for a,b in combinations(start_candidate,2):

        start_team += field[a-1][b-1]
        start_team += field[b-1][a-1]

    for a,b in combinations(link_candidate,2):

        link_team += field[a-1][b-1]
        link_team += field[b-1][a-1]

    result = min(result,abs(start_team-link_team))

print(result)