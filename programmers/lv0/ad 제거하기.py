def solution(strArr):
    answer = []
    for i, string in enumerate(strArr):
        if 'ad' not in string:
            answer.append(string)
    return answer