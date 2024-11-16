def solution(my_string, indices):
    tmp = [char for char in my_string]
    for idx in indices:
        tmp[idx] = 0
    return "".join(list(filter(lambda x: x != 0, tmp)))