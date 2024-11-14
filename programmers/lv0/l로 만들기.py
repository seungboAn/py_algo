def solution(myString):
    answer = []
    for char in myString:
        if char < 'l':
            answer.append('l')
        else:
            answer.append(char)
    return "".join(answer)