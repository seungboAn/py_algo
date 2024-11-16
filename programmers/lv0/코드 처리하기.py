def solution(code):
    answer = []
    mode = 0
    
    for idx, ele in enumerate(code):
        if ele == '1':
            mode = 1 if mode == 0 else 0
        else:
            if mode == 0 and idx % 2 == 0:
                answer.append(ele)
            elif mode == 1 and idx % 2 == 1:
                answer.append(ele)
            else:
                pass
    return "".join(answer) if len(answer) > 0 else "EMPTY"