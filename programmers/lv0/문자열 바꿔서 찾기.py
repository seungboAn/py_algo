def solution(myString, pat):
    tmp = []
    pointer = 0
    answer = 0
    
    for i in range(len(myString)):
        if myString[i] == 'A':
            tmp.append('B')
        else:
            tmp.append('A')
    converted_myString = "".join(tmp)
    while len(converted_myString) - pointer >= len(pat):
        if converted_myString[pointer] != pat[0]:
            pointer += 1
            continue
        else:
            for i in range(len(pat)):
                if converted_myString[pointer + i] != pat[i]:
                    pointer += 1
                    continue
            return 1
    return answer