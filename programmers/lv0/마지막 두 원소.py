def solution(num_list):
    answer = num_list
    res = num_list[-1] - num_list[-2]
    if res > 0:
        answer.append(res)
    else:
        answer.append(num_list[-1] * 2)
    return answer