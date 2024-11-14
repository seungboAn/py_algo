def solution(number):
    sum_list = []
    for num in number:
        sum_list.append(int(num))
    answer = sum(sum_list) % 9
    return answer