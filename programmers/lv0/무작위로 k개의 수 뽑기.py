def solution(arr, k):
    answer = []
    for ele in arr:
        if ele not in answer:
            answer.append(ele)
        if len(answer) == k:
            break
    while len(answer) != k:
        answer.append(-1)
    return answer