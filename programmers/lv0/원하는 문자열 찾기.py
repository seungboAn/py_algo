# https://school.programmers.co.kr/learn/courses/30/lessons/181878
def solution(myString, pat):
    converted_myString = myString.lower()
    converted_pat = pat.lower()
    pointer = 0
    
    while len(converted_myString) - pointer >= len(converted_pat):
        if converted_myString[pointer] != converted_pat[0]:
            pointer += 1
            continue
        else:
            for i in range(len(converted_pat)):
                if converted_myString[pointer + i] != converted_pat[i]:
                    pointer += 1
                    continue
            return 1
    return 0