def solution(n, slicer, num_list):
    slicer = slicer
    n_dict = {
        "1": lambda x: x[:slicer[1] + 1],
        "2": lambda x: x[slicer[0]:],
        "3": lambda x: x[slicer[0]:slicer[1] + 1],
        "4": lambda x: x[slicer[0]:slicer[1] + 1:slicer[2]],
    }
    answer = n_dict[str(n)](num_list)
    return answer