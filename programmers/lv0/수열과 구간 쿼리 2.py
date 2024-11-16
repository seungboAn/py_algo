def solution(arr, queries):
    answer = []
    for query in queries:
        low = 1000000
        for i, ele in enumerate(arr):
            if query[0] <= i and i <= query[1] and ele > query[2] and ele <= low:
                low = ele
        if low == 1000000:
            low = -1
        answer.append(low)
    return answer