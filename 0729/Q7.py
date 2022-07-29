def solution(arr):
    answer = []
    for i in range(len(arr)):
        if len(answer) == 0 or arr[i] != answer[len(answer)-1] : answer.append(arr[i])
    return answer