def solution(arr):
    if len(arr) == 1 : return [-1]
    minimum = arr[0]
    min_index = 0
    
    for i in range(1, len(arr)):
        if minimum > arr[i] :
            minimum = arr[i]
            min_index = i
    del arr[min_index]
    return arr

arr = [4, 3, 2, 1]
answer = solution(arr)
print(answer)