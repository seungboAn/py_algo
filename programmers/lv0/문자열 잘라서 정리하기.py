def solution(myString):
    myString = [string for string in myString.split('x') if string != '']
    return sorted(myString)