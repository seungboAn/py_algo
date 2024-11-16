def solution(rank, attendance):
    answer = 0
    li = sorted([rank[i] for i, ele in enumerate(attendance) if ele == True])
    return ((10000 * rank.index(li[0])) + (100 * rank.index(li[1])) + rank.index(li[2]))