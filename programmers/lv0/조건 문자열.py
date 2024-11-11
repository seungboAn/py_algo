def solution(ineq, eq, n, m):
    oper_tmp = ineq + eq
    operator = {
        "<=": lambda x, y: x <= y,
        ">=": lambda x, y: x >= y,
        "<!": lambda x, y: x < y,
        ">!": lambda x, y: x > y,
    }
    return 1 if operator[oper_tmp](n, m) else 0