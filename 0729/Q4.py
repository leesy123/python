def solution(arr):
    mul = 1
    for i in range(len(arr)):
        m = max(arr)
        mul *= arr[i]
    for i in range(m, mul):
        check = True
        for j in range(len(arr)):
            if i // arr[j] != i / arr[j] : check = False
        if check == True : return i

arr = [2,6,8,14]
answer = solution(arr)
print(answer)