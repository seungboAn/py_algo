def solution(n_str):
    answer = []
    for char in n_str:
        if char == '0' and len(answer) < 1:
            continue
        else:
            answer.append(char)
    return "".join(answer)