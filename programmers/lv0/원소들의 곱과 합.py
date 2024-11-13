import functools

def solution(num_list):
    all_multiple = functools.reduce(lambda x, y: x * y, num_list)
    sum_two_square = functools.reduce(lambda x, y: x + y, num_list) ** 2
    return 1 if all_multiple < sum_two_square else 0