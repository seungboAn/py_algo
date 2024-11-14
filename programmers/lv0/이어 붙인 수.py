def solution(num_list):
    odd_list = []
    even_list = []
    
    for num in num_list:
        if num % 2 == 0:
            even_list.append(str(num))
        else:
            odd_list.append(str(num))
    return int("".join(odd_list)) + int("".join(even_list))