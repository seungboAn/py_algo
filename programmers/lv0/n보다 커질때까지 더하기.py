import functools
import time

# numbers 크기가 커지면 reduce를 중단할 수 있는 방법이 없다.

def solution(numbers, n):
    start = time.time()
    answer = functools.reduce(lambda x, y: x + y if x <= n else x, numbers)
    # answer = 0
    # for i in range(len(numbers)):
    #     if answer <= n:
    #         answer += numbers[i]
    #     else:
    #         break
    end = time.time()
    return answer