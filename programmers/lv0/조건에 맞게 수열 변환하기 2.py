def solution(arr):
    tmp = []
    tmp_next = arr
    count = -1
    
    while tmp != tmp_next:
        count += 1
        tmp = tmp_next
        tmp_next = list(map(lambda x: (x / 2 if (x >= 50 and x % 2 == 0) 
                                 else ((x * 2) + 1 if (x < 50 and x % 2 == 1) 
                                       else x)), tmp_next))
    return count