import functools

def solution(num_list):
    return sum(num_list) if len(num_list) > 10 else functools.reduce(lambda x, y: x * y, num_list)