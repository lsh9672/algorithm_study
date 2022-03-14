#백준 1713번 후보추천하기

'''내가 짠 풀이 - 1등풀이와 7ms 차이 난다.'''
import sys

#사진틀 갯수
n = int(sys.stdin.readline())

#사진틀 - 아무것도 없으면 0
#각각 추천받은 학생, 추천횟수,올라와있는 시간.
photo_frame = [[0,0,0] for _ in range(n)]

all_people = int(sys.stdin.readline())

#추천받은 학생
recommand_people = list(map(int,sys.stdin.readline().split()))


#추천받은 학생을 하나씩 반복함
for i in recommand_people:

    #추천받은 학생이 사진틀안에 있는지 확인.
    #있으면 추천회수 업데이트
    #반복분을 돌면서 찾는다.
    #check가 True이면 추천학생이 사진틀에 없는것.
    check = True
    for j in range(n):
        #있으면 추천수 업데이트 하고 종료
        if photo_frame[j][0] == i:
            check = False
            photo_frame[j][1]+=1
            break

    #추천받은 학생이 사진틀 안에 없으면,
    if check == True:
        #추천수가 작은대로 정렬하고, 같으면 오래된순으로 정렬
        photo_frame.sort(key =lambda x: (x[1],-x[2]))

        #위와 같이 정렬하면 교체또는 삽입위치는 첫번째가 됨.
        #학생교체
        photo_frame[0][0] = i
        
        #추천수 업데이트
        photo_frame[0][1] = 1

        #올라와있는 시간 초기화
        photo_frame[0][2] = 0

    
    #사진틀 전부 돌면서 올라와 있는 시간 업데이트,
    #비어있지 않을때만 업데이트
    for y in range(n):
        if photo_frame[y][0] != 0:
            photo_frame[y][2] += 1


#모든 탐색이 끝나면,학생 번호순대로 정렬후 출력
photo_frame.sort(key = lambda x: (x[0]))

for i in photo_frame:
    if i[0] != 0:
        print(i[0],end=" ")



'''다른사람의 풀이를 참고한 풀이
#위의 풀이에서는 별도의 aging값을 두었는데, 그럴필요 없이, 리스트에 append를 하는식으로 하면, 뒤에 있을수록 오래된것으로 간주할수 있다
#또한 제거한다 하더라고 리스트이므로 제거시 한칸씩 당겨지기 때문에 훨씬 효율적으로 짤수 있다.
import sys

#사진틀 갯수
n = int(sys.stdin.readline())

all_people = int(sys.stdin.readline())

#추천받은 학생
recommand_people = list(map(int,sys.stdin.readline().split()))

photo_frame = list()

recommand_num = list()


for i in recommand_people:
    #추천학생이 사진틀 안에 있으면
    if i in photo_frame:
        recommand_num[photo_frame.index(i)] += 1
    
    #추천학생이 안에 없으면,
    else:
        #빈 공간이 있는지 확인
        #빈공간이 없으면 기존에 있던 것중 추천수가 낮은것을 선택
        if len(photo_frame) >= n:
            min_recommand_index = recommand_num.index(min(recommand_num))
            #같은게 있어도 앞에있는게 먼저 나옴
            #삭제먼저함.
            photo_frame.remove(photo_frame[min_recommand_index])
            recommand_num.remove(recommand_num[min_recommand_index])

            #삭제끝나면 뒤에 새로운 학생 추가.
            photo_frame.append(i)
            recommand_num.append(1)
        
        #빈공간이 있으면 사진틀에 추가
        else:
            photo_frame.append(i)
            recommand_num.append(1)

photo_frame.sort()

print(*photo_frame)
'''