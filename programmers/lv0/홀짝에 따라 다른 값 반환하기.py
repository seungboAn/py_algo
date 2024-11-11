def solution(n):
    res = []
    if n % 2 == 0:
        for i in range(2, n + 1, 2):
            res.append(i ** 2)
    else:
        for i in range(1, n + 1, 2):
            res.append(i)
    return sum(res)