def solution(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)
    
    loop_len = str1_len if str1_len >= str1_len else str1_len < str2_len
    res = []
    for i in range(loop_len):
        res.append(str1[i])
        res.append(str2[i])
    res.append(str1[i + 1:])
    res.append(str2[i + 1:])
    return "".join(res)