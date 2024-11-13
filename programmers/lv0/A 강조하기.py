def solution(myString):
    return "".join(list(map(lambda x: x.upper() if x == 'a' or x == 'A' else x.lower(), myString)))