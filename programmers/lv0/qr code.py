def solution(q, r, code):
    answer = []
    for i, ele in enumerate(code):
        if i % q == r:
            answer.append(ele)
    return "".join(answer)