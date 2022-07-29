def primeNum(n) :
    a = []
    for i in range(2,n+1) :
        check = False
        for j in range(2, int(i**(1/2)) + 1) :
            if i//j == i/j : check = True
        if check==False : a.append(i)
    return a

def Eratos(n) :
    a = [True] * (n+1)
    for i in range (2, int((n+1)**0.5) + 1):
        if a[i] == True :
            for j in range(i+i, n+1, i):
                a[j] = False

    return [i for i in range(2,n+1) if a[i] == True]
            
n = 1000
list = primeNum(n)
list1 = Eratos(n)
for i in range(len(list)):
    print(f'{list[i]} ', end='')
print(f' 총 {len(list)}개')
for i in range(len(list1)):
    print(f'{list1[i]} ', end='')
print(f' 총 {len(list1)}개')