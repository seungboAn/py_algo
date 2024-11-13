def solution(num_list, n):
    pointer = n - 1
    return num_list[pointer + 1:] + num_list[:pointer + 1]