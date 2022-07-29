def solution(numbers):
    return 45 - sum(numbers)

def solution1(numbers):
    answer = 0
    for i in range(10) :
        if i not in numbers: answer += i
    return answer

numbers = [1,2,3,4,6,7,8,0]
answer = solution1(numbers)
print(answer)