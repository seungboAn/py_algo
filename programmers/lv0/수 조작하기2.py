def solution(numLog):
    answer = []
    for i in range(len(numLog) - 1):
        log = numLog[i + 1] - numLog[i]
        if log == 1:
            answer.append('w')
        elif log == -1:
            answer.append('s')
        elif log == 10:
            answer.append('d')
        elif log == -10:
            answer.append('a')
        else:
            pass
    return "".join(answer)