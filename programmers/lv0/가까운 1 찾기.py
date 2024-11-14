def solution(arr, idx):
    pointer = idx
    for i, ele in enumerate(arr):
        if i < idx:
            continue
        else:
            if ele == 1:
                return i
    return -1