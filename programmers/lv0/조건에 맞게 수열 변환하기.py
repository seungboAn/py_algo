def solution(arr, k):
    return list(map(lambda x: x * k if k % 2 == 1 else x + k, arr))