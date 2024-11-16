def solution(arr):
    answer = arr
    max_len = len(answer)
    for row in answer:
        col_len = len(row)
        if max_len <= col_len:
            max_len = col_len
    for i, row in enumerate(answer):
        while len(answer[i]) != max_len:
            answer[i].append(0)
    while len(answer) != max_len:
        answer.append([0 for i in range(max_len)])
    return answer