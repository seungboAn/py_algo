def solution(binomial):
    op_dict = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        "*": lambda x, y: x * y,
    }
    a, op, b = binomial.split()
    return op_dict[op](int(a), int(b))