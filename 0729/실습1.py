def primeNum(n) :
    a = []
    for i in range(2,n+1) :
        check = False
        for j in range(2, int(i**(1/2)) + 1) :
            if i//j == i/j : check = True
        if check==False : a.append(i)
    return a

list = primeNum(1000)
for i in range(len(list)):
    print(f'{list[i]} ', end='')