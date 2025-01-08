from functools import reduce

def find_divisor(n):
    end = n // 2
    divisors = []
    
    for i in range(1, end + 1):
        if n % i == 0:
            divisors.append(i)
    divisors.append(n)
    return divisors

def solution(left, right):
    arr = []
    res = 0
    
    for i in range(left, right + 1):
        arr.append(find_divisor(i))
    for i in arr:
        if len(i) % 2 == 0:
            res += i[-1]
        else:
            res -= i[-1]
    return res
