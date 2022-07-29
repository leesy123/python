num = list(map(int, input().split()))
minimum = num[0]
maximum = num[0]

for i in range(1,len(num)):
    if minimum > num[i] : minimum = num[i]
    if maximum < num[i] : maximum = num[i]
    
print(f'최대값 : {maximum}')
print(f'최소값 : {minimum}')