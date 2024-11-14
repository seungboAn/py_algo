def solution(n):
    answer = []
    for i in range(n):
        tmp = [0 for i in range(n)]
        tmp[i] = 1
        answer.append(tmp)
    return answer