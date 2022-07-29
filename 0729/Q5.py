def solution(n, s):
    answer = []
    maximum = 1
    if s < n : return [-1]
    answer.append(s//2)
    answer.append(s-s//2)
    return answer

n = 2
s = 9
answer = solution(n, s)
print(answer)