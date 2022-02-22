#deepcopy, slicing 속도 측정 - 2차원 리스트로 확인
import time
from copy import deepcopy


# deepcopy로 복사
start_deepcopy_time = time.time()
test_list_1 = [[0 for _ in range(100)] for _ in range(100)]

temp_1 = deepcopy(test_list_1)

end_deepcopy_time = time.time() - start_deepcopy_time

#slicing으로 복사
start_slicing_time = time.time()
test_list_2 = [[0 for _ in range(100)] for _ in range(100)]
temp = []
for i in range(100):
    temp.append(test_list_2[i][:])

end_slicing_time = time.time() - start_slicing_time

print(f"deepcopy : {end_deepcopy_time}")
print(f"slicing  : {end_slicing_time}")

# 슬라이싱이 훨씬 빠르다.

temp[0][0] = 999999
print(test_list_2[0][0])
print(temp[0][0])



