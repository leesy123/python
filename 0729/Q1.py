def result(count, zeros) :
    min_r = 7-count
    max_r = 7-count - zeros
    if min_r > 6 : min_r = 6
    if max_r > 6 : max_r = 6
    print(f'{max_r} {min_r}')

def solution(lottos, win_nums):
    zeros = 0
    count = 0
    
    for i in range(len(lottos)) :
        if lottos[i] == 0 : zeros+=1
        else :
            for j in range(len(win_nums)):
                if lottos[i] == win_nums[j] : count += 1
    result(count, zeros)
    
lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
solution(lottos, win_nums)