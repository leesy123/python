def solution(store, customer):
    answer = []
    for i in range(len(customer)):
        pl = 0
        pr = len(store)-1
        while True :
            pc = (pl+pr)//2
            if store[pc] == customer[i] : 
                answer.append('yes')
                break
            if store[pc] > customer[i] : pr = pc -1
            else : pl = pc + 1
            if pl > pr : 
                answer.append('no')
                break
            
    return answer

store = [2,3,7,8,9]
customer = [7,5,9]
answer = solution(store, customer)
print(answer)