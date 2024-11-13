def solution(num_list):
    odd_list = []
    even_list = []
    for i, num in enumerate(num_list):
        if i % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    return sum(odd_list) if sum(odd_list) >= sum(even_list) else sum(even_list)