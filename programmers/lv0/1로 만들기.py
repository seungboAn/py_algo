def solution(num_list):
    answer = []
    for num in num_list:
        while num != 1:
            if num % 2 == 0:
                num /= 2
            else:
                num = (num - 1) / 2
            answer.append(1)
    return sum(answer)