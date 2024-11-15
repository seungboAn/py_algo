def solution(a, b, c):
    operator_dict = {
        '1': lambda x: sum(x),
        '2': lambda x: sum(x) * sum([i * i for i in x]),
        '3': lambda x: sum(x) * sum([i * i for i in x]) * sum([i * i * i for i in x]),
    }
    same_count = 0
    if a != b and b != c and a != c:
        same_count = 1
    if (a != c and a != b and b == c) or (a == c and a != b and b != c) or (a != c and b != c and a == b):
        same_count = 2
    if a == b and b == c and a == c:
        same_count = 3
    return operator_dict[str(same_count)]([a, b, c])