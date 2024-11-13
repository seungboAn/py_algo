def solution(my_string, is_suffix):
    if len(is_suffix) > len(my_string):
        return 0
    for i in range(len(is_suffix)):
        if is_suffix[-(i + 1)] != my_string[-(i + 1)]:
            return 0
    return 1