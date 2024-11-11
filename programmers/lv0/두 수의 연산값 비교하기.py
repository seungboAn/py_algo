def solution(a, b):
    custom_operator = int(str(a) + str(b))
    multiple_two_operator = 2 * a * b
    return custom_operator if custom_operator >= multiple_two_operator else multiple_two_operator