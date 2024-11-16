def solution(myString, pat):
    pointer = 0
    len_pat = len(pat)
    answer = []
    flag = False
    
    for i, char in enumerate(myString):
        if char != pat[0]:
            if flag == False:
                answer.append(char)
            pointer += 1
        else:
            if myString[i:i + len_pat] != pat:
                answer.append(myString[i:i + len_pat])
            else:
                answer.append(pat)
                flag = True
            pointer += len_pat
    return "".join(answer)