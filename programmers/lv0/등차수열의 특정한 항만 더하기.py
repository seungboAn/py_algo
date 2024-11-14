def solution(a, d, included):
    answer = [ a + (i * d) for i, ele in enumerate(included) if ele == True]
    return sum(answer)