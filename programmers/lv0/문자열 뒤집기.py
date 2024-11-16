def solution(my_string, s, e):
    answer = []
    target = [i for i in my_string[s:e + 1]][::-1]
    answer.append(my_string[:s])
    answer.append("".join(target))
    answer.append(my_string[e + 1:])
    return "".join(answer)