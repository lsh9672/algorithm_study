#파이썬 속도 테스트 - 함수안에서 반복문 실행과 함수 밖에서 반복문 실행
import time



def test_in_function1():

    for i in range(100000):
        pass


start_time_in_function = time.time()

test_in_function1()

end_time_in_function = time.time() - start_time_in_function


start_time_in_global = time.time()
for i in range(100000):
        pass
end_time_in_global = time.time() - start_time_in_global




print(f"iter in func : {end_time_in_function}")
print(f"iter not in func : {end_time_in_global}")