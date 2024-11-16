def solution(arr, queries):
    answer = arr
    for query in queries:
        for i in range(len(answer)):
            if query[0] <= i and i <= query[1] and i % query[2] == 0:
                answer[i] += 1
    return answer