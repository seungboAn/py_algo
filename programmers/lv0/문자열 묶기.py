from collections import Counter

def solution(strArr):
    answer = 0
    result = Counter([len(string) for string in strArr])
    for key, value in result.items():
        if value >= answer:
            answer = value
    return answer