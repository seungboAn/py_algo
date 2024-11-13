def solution(n, control):
    answer = n
    command_dict = {
        'w': lambda x: x + 1,
        's': lambda x: x - 1,
        'd': lambda x: x + 10,
        'a': lambda x: x - 10,
    }
    for command in control:
        answer = command_dict[command](answer)
    return answer