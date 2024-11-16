def solution(my_string, queries):
    answer = [char for char in my_string]
    for query in queries:
        target = answer[query[0]:query[1] + 1]
        answer[query[0]:query[1] + 1] = target[::-1]
    return "".join(answer)