def solution(num_list):
    iter = enumerate(num_list)
    for i in range(len(num_list)):
        idx, curr = next(iter)
        if curr < 0:
            return idx
    return -1