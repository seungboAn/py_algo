def solution(str_list):
    answer = []
    for i, ele in enumerate(str_list):
        if ele == 'l':
            answer = str_list[:i]
            break
        elif ele == 'r':
            answer = str_list[i + 1:]
            break
    return answer