def solution(my_string):
    alphabet_dict = {}
    answer = []
    for i in range(26):
        key = chr(ord('A') + i)
        value = 0
        alphabet_dict.update({key: value})
    for i in range(26):
        key = chr(ord('a') + i)
        value = 0
        alphabet_dict.update({key: value})
    for ele in my_string:
        alphabet_dict[ele] += 1
    for key, value in alphabet_dict.items():
        answer.append(value)
    return answer