#백준 10546번(자료구조, 실버4)
import sys


n = int(sys.stdin.readline())

participant_dict = dict()

for _ in range(n):
    temp = sys.stdin.readline().strip()

    if temp not in participant_dict:
        participant_dict[temp] = 1

    else:
        participant_dict[temp] += 1

for _ in range(n-1):

    temp = sys.stdin.readline().strip()

    participant_dict[temp] -=1
    if participant_dict[temp] == 0:
        del participant_dict[temp]


print(list(participant_dict.keys())[0])
