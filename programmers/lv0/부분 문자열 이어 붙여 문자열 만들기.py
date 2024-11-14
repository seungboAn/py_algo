def solution(my_strings, parts):
    answer = [my_strings[i][parts[i][0]:parts[i][1] + 1] for i, string in enumerate(my_strings)]
    return "".join(answer)