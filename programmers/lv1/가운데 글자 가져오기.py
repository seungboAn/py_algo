def solution(s):
    len_s = len(s)
    target_index = len_s // 2
    
    if len_s % 2 == 0:
        return s[target_index - 1] + s[target_index] 
    return s[target_index]