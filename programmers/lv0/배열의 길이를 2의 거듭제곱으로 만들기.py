# log, ceil, is_integer()
import math

def solution(arr):
    answer = arr
    log_value = math.log2(len(answer))
    if log_value.is_integer():
        return answer
    else:
        while len(answer) < 2 ** (math.ceil(log_value)):
            answer.append(0)
    return answer