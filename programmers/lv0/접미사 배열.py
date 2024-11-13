def solution(my_string):
    res = [my_string[-i:] for i, char in enumerate(my_string)]
    return sorted(res)