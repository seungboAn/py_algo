def solution(todo_list, finished):
    answer = []
    for i, todo in enumerate(todo_list):
        if finished[i] == False:
            answer.append(todo)
    return answer