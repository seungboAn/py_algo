def solution(arr, n):
    answer = []
    len_arr = len(arr)
    for i, ele in enumerate(arr):
        if len_arr % 2 == 1:
            if i % 2 == 0:
                answer.append(ele + n)
            else:
                answer.append(ele)
        else:
            if i % 2 == 1:
                answer.append(ele + n)
            else:
                answer.append(ele)
    return answer