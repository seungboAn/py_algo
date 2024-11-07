def solution(my_string, overwrite_string, s):
    overwrite_idx = 0
    answer = []
    for i in range(len(my_string)):
        if i < s:
            answer.append(my_string[i])
        elif i >= s and overwrite_idx < len(overwrite_string):
            answer.append(overwrite_string[overwrite_idx])
            overwrite_idx += 1
        else:
            answer.append(my_string[i])
    return "".join(answer)