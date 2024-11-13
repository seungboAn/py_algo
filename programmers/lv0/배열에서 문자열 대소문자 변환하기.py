# https://school.programmers.co.kr/learn/courses/30/lessons/181875
def solution(strArr):
    result = [x.swapcase() if i % 2 == 0 else x for i, x in enumerate(strArr)]
    return result