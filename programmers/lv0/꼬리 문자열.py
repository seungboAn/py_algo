def solution(str_list, ex):
    return "".join(list(filter(lambda x: "" if ex in x else x, str_list)))